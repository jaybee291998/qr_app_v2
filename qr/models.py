from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class ContactInformation(models.Model):

    class Sex(models.TextChoices):
        MALE            = 'M', _('Male')
        FEMALE          = 'F', _('Female')
    first_name 			= models.CharField(max_length=32)
    last_name           = models.CharField(max_length=32)
    sex                 = models.CharField(max_length=1, choices=Sex.choices, default=Sex.MALE)
    address             = models.CharField(max_length=128)
    phone               = models.CharField(max_length=11)
    email               = models.CharField(max_length=64)
    birthdate           = models.DateField()
    qr_code             = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Log(models.Model):
    qr_code             = models.CharField(max_length=6)
    temperature         = models.DecimalField(max_digits=3, decimal_places=1)
    date                = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.qr_code} {self.temperature}: {self.date}'

class QRRequest(models.Model):
    contact         = models.ForeignKey(ContactInformation, related_name="qr_request", on_delete=models.CASCADE, null=True)
    latitude        = models.CharField(max_length=100)
    longitude       = models.CharField(max_length=100)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.contact.first_name} {self.contact.last_name} - {self.timestamp}'