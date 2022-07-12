from django.db import models
from django.forms import FileField

# Create your models here.


class MyFile(models.Model):
    name = models.CharField(max_length=100)
    FileField = models.FileField(upload_to="media/nft")