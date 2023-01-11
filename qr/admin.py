from django.contrib import admin
from .models import ContactInformation, Log, QRRequest

# Register your models here.
admin.site.register(ContactInformation)
admin.site.register(Log)
admin.site.register(QRRequest)