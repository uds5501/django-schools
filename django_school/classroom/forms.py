from django import forms
from .models import ClassRoom

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        widgets = {'school': forms.HiddenInput()}
        fields = ('school', 'name', ) # '__all__' #('name', )