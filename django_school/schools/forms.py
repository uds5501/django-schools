from django.contrib.auth.forms import UserCreationForm
from .models import School,User
from django import forms
class CustomUserCreationForm(UserCreationForm):
    school = forms.ModelChoiceField(
        queryset=School.objects.all(),
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User #settings.AUTH_USER_MODEL

    def save(self, commit=True):
        user = super().save(commit=False)
        user.school = self.cleaned_data.get('school')
        return user

    def clean_username(self, *args, **kargs):
        error = False
        username = self.cleaned_data['username'].lower()

        # usernames not allowed since they are used as base urls
        base_urls = ['admin','students','teachers','quizzes','accounts']
        if username in base_urls:
        	error = "Usernames such as %s are not allowed" %','.join(base_urls)        	
        elif len(username) < 3:
        	error = "Username must be at least 3 characters"

        if error: raise forms.ValidationError(error)
        return self.cleaned_data['username']