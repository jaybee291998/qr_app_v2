from django.db import models

# Create your models here.
class ContactInfomation(models.Model):
	first_name 			= models.CharField(max_length=32)
    last_name           = models.CharField(max_length=32)
    address             = models.CharField(max_length=128)
    phone               = models.CharField(max_length=11)
    email               = models.CharField(max_length=64)
    birthdate           = models.DateFiels()
    qr_code             = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
