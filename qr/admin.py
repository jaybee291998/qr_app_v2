from django.contrib import admin
from .models import ContactInformation, Log

# Register your models here.
admin.site.register(ContactInformation)
admin.site.register(Log)