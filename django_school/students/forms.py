from django import forms
from schools.forms import CustomUserCreationForm
from quizzes.models import Subject
from django.db import transaction
from .models import Student
from classroom.models import ClassRoom

class StudentSignUpForm(CustomUserCreationForm):
    classroom = forms.CharField(required=True,
        widget=forms.Select(attrs={'required': 'required'}))
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     required=True
    # )
    
    def clean_classroom(self):
        # print (self.cleaned_data['classroom'])
        return self.cleaned_data['classroom']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 1 # student
        #user.is_active = False
        #user.school = self.cleaned_data.get('school')
        user.save()
        classroom = ClassRoom.objects.get(id= self.cleaned_data.get('classroom'))
        student = Student.objects.create(user=user,classroom = classroom)
        # student.interests.add(*self.cleaned_data.get('interests'))
        
        # course.students.add(user)
        return user
