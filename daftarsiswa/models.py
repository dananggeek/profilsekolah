from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class pendaftaran (models.Model):
    #user            =models.ForeignKey(User, on_delete=models.CASCADE)
    nama_depan           =models.CharField(max_length=50)
    nama_belakang           =models.CharField(max_length=50)
    email           =models.CharField(max_length=50)
    foto            =models.FileField()
    alamat          =models.CharField(max_length=100)
    tempat_lahir    =models.CharField(max_length=50)
    tanggal_lahir   =models.DateField()
    agama           =models.CharField(max_length=50)
    nohp            =models.IntegerField()
    nilai_un        =models.FileField()
    nama_orangtua   =models.CharField(max_length=50)
    alamat_orangtua =models.CharField(max_length=50)
    nohp_orangtua   =models.IntegerField()
    tanggal_daftar  =models.DateTimeField(auto_now=False,auto_now_add=True)
      #timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)
    status_terima   =models.BooleanField(default=False)

    def __str__(self):
        return self.nama_depan
