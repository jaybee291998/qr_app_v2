from django import forms
from django.contrib.admin import widgets
from .models import ContactInformation

class RegistrationForm(forms.ModelForm):
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