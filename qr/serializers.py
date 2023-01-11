from rest_framework import serializers
from .models import ContactInformation, Log, QRRequest

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
			'qr_code'
		]

class LogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Log
		fields = ['qr_code', 'temperature', 'date']

class QRRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = QRRequest
		fields = '__all__'