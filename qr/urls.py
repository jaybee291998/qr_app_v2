from django.urls import path
from .views import qr_scanner_view, ContactCreateView
from . import views as v

urlpatterns = [
    path('qr_scanner/', qr_scanner_view, name='qr_scanner'),
    path('registration/', ContactCreateView.as_view(), name='registration'),
    path('get_qr_code', v.get_qr_code_view, name='get_qr_code'),
    path('get_qr_code_api/', v.get_qr_code, name='get_qr_code_api'),
    path('log_list_api/', v.LogList.as_view(), name='log_list_api'),
    path('get_log_list_api/', v.get_log_list_api, name='get_log_list_api'),
    path('get_log_list/', v.get_log_list_view, name='get_log_list')
]