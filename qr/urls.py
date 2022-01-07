from django.urls import path
from .views import qr_scanner_view

urlpatterns = [
    path('index/', qr_scanner_view, name='qr_scanner'),
]