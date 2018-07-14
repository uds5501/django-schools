from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.conf import settings

from .models import Student
from schools.models import School,User
from quizzes.models import Subject

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
        user.user_type = 1
        user.school = self.cleaned_data.get('schools')
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user


