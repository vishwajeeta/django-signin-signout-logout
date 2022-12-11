from distutils.command.upload import upload
import email
from django.db import models
from sqlalchemy import desc
from django.db import models
# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img  =models.ImageField(upload_to='pics')
    clas = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contract = models.IntegerField(10)
    more =models.BooleanField(default=False)


    