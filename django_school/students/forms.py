from django import forms
from schools.forms import CustomUserCreationForm
from quizzes.models import Subject
from django.db import transaction
from .models import Student

class StudentSignUpForm(CustomUserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 1 # student
        #user.is_active = False
        #user.school = self.cleaned_data.get('school')
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user

