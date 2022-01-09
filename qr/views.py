from datetime import date, datetime, timedelta

from django.shortcuts import render
from qr_app.base_classes import BaseCreateView

from django.urls import reverse_lazy
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import ContactInformation, Log
from .forms import RegistrationForm
from .serializers import ContactSerializer, LogSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

def qr_scanner_view(request):
	context = {
		'domain': reverse_lazy('log_list_api')
	}
	return render(request, 'qr/qr_scanner.html', context)

class ContactCreateView(BaseCreateView):
	model = ContactInformation
	template_name = 'qr/registration.html'
	success_url = reverse_lazy('get_qr_code')
	form_class = RegistrationForm

def get_qr_code_view(request):
	context = {
		'domain':reverse_lazy('get_qr_code_api')
	}
	return render(request, 'qr/get_qr_code.html', context)

def get_qr_code(request):
	if request.method == 'GET':
		email = request.GET.get('email')
		phone = request.GET.get('phone')

		contact = ContactInformation.objects.get(email=email, phone=phone)
		serializer = ContactSerializer(contact)

		return JsonResponse(serializer.data)
	return JsonResponse({'message':'no data'})

# api
# api for posting log data
class LogList(APIView):
	def get(self, request, format=None):
		logs = Log.objects.filter(date=date.today())
		serializer = LogSerializer(logs, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = LogSerializer(data=request.data)
		if serializer.is_valid():
			qr_code = serializer.validated_data['qr_code']
			contact_info = ContactInformation.objects.get(qr_code=qr_code)
			print(contact_info)
			if contact_info is not None:
				contact_serializer = ContactSerializer(contact_info)
				serializer.save()
				return Response(contact_serializer.data, status=status.HTTP_201_CREATED)
			error = {
				'errors': 'QR code is not registered'
			}
			return JsonResponse(error)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

