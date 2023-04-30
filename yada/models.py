from django.db import models

# Create your models here.
class YadaFp(models.Model):
    # name of person
    name = models.CharField(max_length=200)
    # phone number
    phone = models.CharField(max_length=100)
    # adress of their home or hometown
    address = models.CharField(max_length=200)
    # how was service or Food Pantry?
    service = models.CharField(max_length=300)
    # possible text for chat
    text = models.CharField(max_length=350)
    # date 
    date = models.CharField(max_length=100)
    ## Volunteer Signup ##
    signName = models.CharField(max_length=200)
    ## Volunteer phone ##
    signPhone = models.CharField(max_length=100)
    ## Volunteer Date ##
    signDate = models.CharField(max_length=100)