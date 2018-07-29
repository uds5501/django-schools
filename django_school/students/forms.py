from django import forms
from schools.forms import CustomUserCreationForm
from quizzes.models import Subject
from django.db import transaction
from .models import Student
from schools.models import Course

class StudentSignUpForm(CustomUserCreationForm):
    course = forms.CharField(required=True,
        widget=forms.Select(attrs={'required': 'required'}))
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        required=True
    )
    
    def clean_course(self):
        print (self.cleaned_data['course'])
        return self.cleaned_data['course']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 1 # student
        #user.is_active = False
        #user.school = self.cleaned_data.get('school')
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        course = Course.objects.get(id= self.cleaned_data.get('course'))
        course.students.add(user)
        return user
