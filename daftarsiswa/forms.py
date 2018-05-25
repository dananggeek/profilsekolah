from django.db import models
from django import forms
from . models import *

class PendaftaranForm(forms.Form):
    nama_depan      =forms.CharField(max_length=50)
    nama_belakang   =forms.CharField(max_length=50)
    kelamin         =forms.CharField(max_length=12)
    email           =forms.CharField(max_length=50)
    foto            =forms.FileField()
    alamat          =forms.CharField(max_length=100)
    tempat_lahir    =forms.CharField(max_length=50)
    tanggal_lahir   =forms.DateField()
    agama           =forms.CharField(max_length=50)
    nohp            =forms.IntegerField()
    nilai_un        =forms.FileField()
    nama_orangtua   =forms.CharField(max_length=50)
    alamat_orangtua =forms.CharField(max_length=50)
    nohp_orangtua   =forms.IntegerField()
    tanggal_daftar  =forms.DateField()

#nama Belakang , Kelamin, email
#forms.DateField(widget=forms.DateInput(format='%m/%d/%Y')), input_formats=('%m/%d/%Y',))
