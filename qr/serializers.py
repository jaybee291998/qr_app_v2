from rest_framework import serializers
from .models import ContactInformation

class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContactInformation
		fields = [
			'first_name',
			'last_name',
			'sex',
			'address',
			'phone',
			'email',
			'birthdate',
			'qr_code',
		]
