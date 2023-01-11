from datetime import date, datetime, timedelta

from django.shortcuts import render
from qr_app.base_classes import BaseCreateView

from django.urls import reverse_lazy
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import ContactInformation, Log, QRRequest
from .forms import RegistrationForm
from .serializers import ContactSerializer, LogSerializer, QRRequestSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

def qr_scanner_view(request):
	context = {
		'domain': reverse_lazy('log_list_api'),
		'home_domain': reverse_lazy('home')
	}
	return render(request, 'qr/qr_scanner.html', context)

class ContactCreateView(BaseCreateView):
	model = ContactInformation
	template_name = 'qr/registration.html'
	success_url = reverse_lazy('get_qr_code')
	form_class = RegistrationForm

def get_qr_code_view(request):
	context = {
		'domain':reverse_lazy('get_qr_code_api'),
		'home_domain': reverse_lazy('home')
	}
	return render(request, 'qr/get_qr_code.html', context)

def get_log_list_view(request):
	context = {
		'domain':reverse_lazy('get_log_list_api'),
		'home_domain': reverse_lazy('home')
	}
	return render(request, 'qr/get_log_list.html', context)

def get_qr_code(request):
	if request.method == 'GET':
		email = request.GET.get('email')
		phone = request.GET.get('phone')
		latitude = request.GET.get('latitude')
		longitude = request.GET.get('longitude')
		try:
			contact = ContactInformation.objects.get(email=email, phone=phone)
		except ContactInformation.DoesNotExist:
			contact = None
		if contact is not None:
			serializer = ContactSerializer(contact)
			d = {
				'latitude': float(latitude),
				'longitude': float(longitude)
			}
			print(d)
			qr_request_serializer = QRRequestSerializer(data=d)
			if qr_request_serializer.is_valid():
				qr_request_serializer.save(contact=contact)
			return JsonResponse(serializer.data)
	return JsonResponse({'message':'no data'})

# view for home
def home_view(request):
	context = {
		'qr_scanner_domain': reverse_lazy('qr_scanner'),
		'registration_domain': reverse_lazy('registration'),
		'get_qr_code_domain': reverse_lazy('get_qr_code'),
		'log_list' : reverse_lazy('get_log_list')
	}

	return render(request, 'qr/home.html', context)



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
			contact_info = ContactInformation.objects.filter(qr_code=qr_code)
			if contact_info.exists():
				contact_serializer = ContactSerializer(contact_info.first())
				serializer.save()
				return Response(contact_serializer.data, status=status.HTTP_201_CREATED)
			error = {
				'errors': 'QR code is not registered'
			}
			return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_log_list_api(request):
	date_entry = date.today()
	logs = Log.objects.filter(date__year=date_entry.year, date__month=date_entry.month, date__day=date_entry.day)
	serializer = LogSerializer(logs, many=True)

	qr_codes = list(set([log.qr_code for log in logs]))
	contacts = {}
	for qr_code in qr_codes:
		contact = ContactInformation.objects.get(qr_code=qr_code)
		contact_serializer = ContactSerializer(contact)
		contacts[qr_code] = contact_serializer.data

	data = {
		'contacts':contacts,
		'logs': serializer.data
	}

	return JsonResponse(data)

