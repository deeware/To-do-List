from django import forms
from django.forms import ModelForm

from .models import * 

# Both these Classes will allow capturing date & time in HTML5 way
class DateInput(forms.DateInput):
	input_type='date'
class TimeInput(forms.TimeInput):
	input_type='time'

class TaskForm(forms.ModelForm):
	title=forms.CharField(label="Your Task goes here ",max_length=200,
		widget=forms.TextInput(attrs={'class':'form-control','style':'width:50%'}))
	date=forms.DateField(label="Date ",widget=DateInput(attrs={'class':'form-control','style':'width:25%'}))
	time=forms.TimeField(label="Time ",widget=TimeInput(attrs={'class':'form-control','style':'width:25%'}))

	class Meta:
		model = Tasks
		fields = ('title','date','time')

		
