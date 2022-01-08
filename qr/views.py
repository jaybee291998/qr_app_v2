from django.shortcuts import render
from qr_app.base_classes import BaseCreatView

from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import ContactInformation, Log
from .forms import RegistrationForm
# Create your views here.

def qr_scanner_view(request):
	return render(request, 'qr/index.html', {})

class ContactCreateView(BaseCreatView):
	model = ContactInformation
	template_name = 'qr/registration.html'
	success_url = reverse_lazy('qr_scanner')
	form_class = RegistrationForm

