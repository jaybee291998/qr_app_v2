from django import forms
from django.contrib.admin import widgets
from .models import ContactInformation

class DateTimeInput(forms.DateTimeInput):
	input_type='datetime-local'

class RegistrationForm(forms.ModelForm):
	birthdate 		= froms.DateField(widget=DateTimeInput)
	class Meta:
		model = ContactInformation
		fields = [
			'first_name',
			'last_name',
			'sex',
			'address',
			'phone',
			'email',
			'birthdate'
		]