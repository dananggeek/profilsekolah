from django.db import models

# Create your models here.
class Calender(models.Model):
    judul       =models.CharField(max_length=30)
    slug        =models.SlugField(unique=True)
    publish     =models.DateTimeField()
    jadwal_acara=models.DateTimeField()
    ahir_acara  =models.DateTimeField()
    deskripsi   =models.TextField()
    gambar      =models.FileField(blank=True)
    lokasi      =models.TextField()

    def __str__ (self):
        return self.judul
