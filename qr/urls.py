from django.urls import path
from .views import qr_scanner_view, ContactCreateView

urlpatterns = [
    path('index/', qr_scanner_view, name='qr_scanner'),
    path('registration/', ContactCreateView.as_view(), name='registration')
]