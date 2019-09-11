from django import forms
from .models import ClassRoom, Period, Subject

class ClassroomForm(forms.ModelForm):
    def clean_division(self):
        """To prevent classroom names 10A, 10a"""
        data = self.cleaned_data['division']
        return data.upper()

    class Meta:
        model = ClassRoom
        # this is required for unique together validation
        widgets = {'school': forms.HiddenInput()}
        fields = ('school', 'name','division' ) # '__all__' #('name', )

class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = '__all__' #('name', )

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        widgets = {'school': forms.HiddenInput()}
        fields = ('school', 'name', ) # '__all__' #('name', )
