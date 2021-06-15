from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils import timezone
# Create your models here.
class Lottery(models.Model):
    url     = models.URLField(max_length=500)
    content = models.CharField(max_length=500)
    url_pic   = models.CharField(max_length=500)
    follow_account = models.CharField(max_length=500)
    message = models.CharField(max_length=500)

