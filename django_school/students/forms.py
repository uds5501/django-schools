from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Student, StudentAnswer
from schools.models import School,Subject,User
from django.conf import settings

from quizzes.models import Answer

class StudentSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    schools = forms.ModelChoiceField(
        queryset=School.objects.all(),
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User #settings.AUTH_USER_MODEL

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.school = self.cleaned_data.get('schools')
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user


class StudentInterestsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('interests', )
        widgets = {
            'interests': forms.CheckboxSelectMultiple
        }


class TakeQuizForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None)

    class Meta:
        model = StudentAnswer
        fields = ('answer', )

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answers.order_by('text')
