from django import forms
from django.contrib.auth.forms import UserCreationForm
from schools.models import School,User

class TeacherSignUpForm(UserCreationForm):
    schools = forms.ModelChoiceField(
        queryset=School.objects.all(),
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User #settings.AUTH_USER_MODEL

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2
        user.school = self.cleaned_data.get('schools')
        if commit:
            user.save()
        return user
