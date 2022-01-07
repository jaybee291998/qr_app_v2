from django.shortcuts import render

# Create your views here.

def qr_scanner_view(request):
	return render(request, 'qr/index.html', {})