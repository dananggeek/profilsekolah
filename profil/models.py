from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Banner(models.Model):
    #question_text = models.CharField(max_length=200)
    nama =models.CharField(max_length=200)
    gambar = models.FileField()
    text = models.TextField()

    def __str__(self):
        return self.nama

class About(models.Model):
    email =models.CharField(max_length=200)
    nohp =models.IntegerField(default=0)
    alamat =models.CharField(max_length=100)
    visi=models.TextField()

    def __str__(self):
        return self.email
 

class why(models.Model):
    icon = models.FileField()
    content = models.CharField(max_length=140)
    name= models.CharField(max_length=30)
