from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView,ListView
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from .decorators import teacher_required
from .forms import TeacherSignUpForm
from quizzes.forms import BaseAnswerInlineFormSet, QuestionForm
from quizzes.models import Answer, Question, Quiz

from students.models import Student
from django.views import View
from schools.models import User

class TeacherSignUpView(CreateView):
    model = settings.AUTH_USER_MODEL
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['usertype'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class StudentList(View):
    def get(self, request):
        queryset = Student.objects.filter(user__school = request.user.school)
        return render(request,'teachers/students.html',{'students':queryset})

    def post(self,request):
        user_id = request.POST.get('user','')
        verified = request.POST.get('verified', '')
        if user_id:
            user = User.objects.get(id = user_id)
            if verified == 'on': 
                user.is_verified = True
            else:
                user.is_verified = False
            user.save()

        return redirect('teachers:student_list')

        
@login_required
@teacher_required
def question_add(request, pk):
    # By filtering the quiz by the url keyword argument `pk` and
    # by the owner, which is the logged in user, we are protecting
    # this view at the object-level. Meaning only the owner of
    # quiz will be able to add questions to it.
    quiz = get_object_or_404(Quiz, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            messages.success(request, 'You may now add answers/options to the question.')
            return redirect('question_change', quiz.pk, question.pk)
    else:
        form = QuestionForm()

    return render(request, 'teachers/question_add_form.html', {'quiz': quiz, 'form': form})


@login_required
@teacher_required
def question_change(request, quiz_pk, question_pk):
    # Simlar to the `question_add` view, this view is also managing
    # the permissions at object-level. By querying both `quiz` and
    # `question` we are making sure only the owner of the quiz can
    # change its details and also only questions that belongs to this
    # specific quiz can be changed via this url (in cases where the
    # user might have forged/player with the url params.
    quiz = get_object_or_404(Quiz, pk=quiz_pk, owner=request.user)
    question = get_object_or_404(Question, pk=question_pk, quiz=quiz)

    AnswerFormSet = inlineformset_factory(
        Question,  # parent model
        Answer,  # base model
        formset=BaseAnswerInlineFormSet,
        fields=('text', 'is_correct'),
        min_num=2,
        validate_min=True,
        max_num=10,
        validate_max=True
    )

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        formset = AnswerFormSet(request.POST, instance=question)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form.save()
                formset.save()
            messages.success(request, 'Question and answers saved with success!')
            return redirect('quiz_change', quiz.pk)
    else:
        form = QuestionForm(instance=question)
        formset = AnswerFormSet(instance=question)

    return render(request, 'teachers/question_change_form.html', {
        'quiz': quiz,
        'question': question,
        'form': form,
        'formset': formset
    })