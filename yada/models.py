from django.db import models

# Create your models here.
class YadaFp(models.Model):
    # name of person
    name = models.CharField(max_length=200)
    # phone number
    phone = models.CharField(max_length=100)
   