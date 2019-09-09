from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from teachers.decorators import teacher_required

from classroom.forms import SubjectForm
from classroom.models import Subject

@login_required
@teacher_required
def subject_view(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.school = request.user.school
            subject.save()
            messages.success(request, 'Subject saved with success!')
            return redirect('classroom:subjects')
    else:
        subject = Subject(school = request.user.school)
        form = SubjectForm(instance=subject)

    subjects = Subject.objects.filter(school = request.user.school)
    return render(request,"classroom/subjects.html", {'form': form, 'subjects':subjects })
