from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Guru (models.Model):
    user_guru       =   models.ForeignKey(User, on_delete=models.CASCADE)
    nip             =  models.CharField(max_length=12)
    nama            =  models.CharField(max_length=25)
    no_hp           =  models.IntegerField()
    email           =  models.CharField(max_length=12)
    foto_guru       =  models.FileField()
    alamat          =  models.TextField()

    def __str__(self):
        return self.nama

class Kelas (models.Model):

    nama_kelas      =   models.CharField(max_length=20)
    nama_guru_wali           =   models.ForeignKey(Guru, on_delete=models.CASCADE)
    jurusan         =   models.CharField(max_length=20)

    def __str__(self):
        return self.nama_kelas

class Siswa  (models.Model):
    kelas           =   models.ForeignKey(Kelas, on_delete=models.CASCADE)
    NIS             =   models.IntegerField()
    NISN            =   models.IntegerField()
    nama_siswa      =   models.CharField(max_length=50)
    foto_siswa      =   models.FileField()
    alamat_asal     =   models.TextField()
    alamat_tinggal  =   models.TextField()
    no_hp           =   models.IntegerField()
    email           =   models.CharField(max_length=23)
    nama_orangtua   =   models.CharField(max_length=50)
    catatan         =   models.TextField()

    def __str__(self):
        return self.nama_siswa
