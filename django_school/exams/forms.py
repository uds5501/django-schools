from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        # widgets = {'school': forms.HiddenInput()}
        fields = ('name','exam_class','exam_date','is_grade') # '__all__' #('name', )