from schools.forms import CustomUserCreationForm

class TeacherSignUpForm(CustomUserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2 # teacher
        #user.is_active = False
        if commit:
            user.save()
        return user
