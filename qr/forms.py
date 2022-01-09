from django import forms
from django.contrib.admin import widgets
from .models import ContactInformation

class DateTimeInput(forms.DateInput):
	input_type='date'

class RegistrationForm(forms.ModelForm):
	birthdate 		= forms.DateField(widget=DateTimeInput)
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

	def clean(self, *args, **kwargs):
		cleaned_data = super().clean()
		first_name 		= cleaned_data['first_name']
		last_name 		= cleaned_data['last_name']
		email 			= cleaned_data['email']
		phone 			= cleaned_data['phone']
		if ContactInformation.objects.filter(first_name=first_name, last_name=last_name, email=email, phone=phone).exists():
			raise forms.ValidationError(f'The user is already registered in the system.')
		return super(RegistrationForm, self).clean(*args, **kwargs)