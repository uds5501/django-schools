from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from teachers.decorators import teacher_required

from .forms import ExamForm
from .models import Exam

@login_required
@teacher_required
def exam_view(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.school = request.user.school
            exam.academicyear = request.user.school
            exam.save()
            messages.success(request, 'Exam saved with success!')
            return redirect('exams:exam')
    else:
        # classroom = ClassRoom(school = request.user.school)
        form = ExamForm()

    exams = Exam.objects.filter(school = request.user.school)
    return render(request,"exams/exams.html", {'form': form, 'exams':exams })
