from django.shortcuts import render
from qr_app.base_classes import BaseCreateView

from django.urls import reverse_lazy
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import ContactInformation, Log
from .forms import RegistrationForm
from .serializers import ContactSerializer
# Create your views here.

def qr_scanner_view(request):
	return render(request, 'qr/index.html', {})

class ContactCreateView(BaseCreateView):
	model = ContactInformation
	template_name = 'qr/registration.html'
	success_url = reverse_lazy('qr_scanner')
	form_class = RegistrationForm

def get_qr_code_view(request):
	context = {
		'domain':reverse_lazy('get_qr_code_api')
	}
	return render(request, 'qr/get_qr_code.html', {})

def get_qr_code(request):
	if request.method == 'GET':
		email = request.GET.get('email')
		phone = request.GET.get('phone')

		contact = ContactInformation.objects.get(email=email, phone=phone)
		serializer = ContactSerializer(contact)

		return serializer.data
	return JsonResponse({'message':'no data'})

