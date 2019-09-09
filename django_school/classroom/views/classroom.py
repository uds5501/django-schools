from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from teachers.decorators import teacher_required

from classroom.forms import ClassroomForm
from classroom.models import ClassRoom

@login_required
@teacher_required
def classroom_view(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.school = request.user.school
            classroom.save()
            messages.success(request, 'ClassRoom saved with success!')
            return redirect('classroom:classrooms')
    else:
        classroom = ClassRoom(school = request.user.school)
        form = ClassroomForm(instance=classroom)

    classrooms = ClassRoom.objects.filter(school = request.user.school)
    return render(request,"classroom/classrooms.html", {'form': form, 'classrooms':classrooms })
