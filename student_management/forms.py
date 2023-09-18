from django import forms
from .models import *
from django.forms.widgets import DateInput

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Student
        exclude = ['matriculation_number','status']
        # fields = '__all__'
