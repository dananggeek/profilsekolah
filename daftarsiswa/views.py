from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . models import *
from . forms import *
from django.contrib import messages
# Create your views here.
def add(request):
    form=PendaftaranForm(request.POST, request.FILES or None)
    if request.method =='POST':


            nama_depan=request.POST['nama_depan']
            nama_belakang= request.POST['nama_belakang']
            email= request.POST['email']
            foto= request.FILES['foto']
            alamat= request.POST['alamat']
            tempat_lahir= request.POST['tempat_lahir']
            tanggal_lahir= request.POST['tanggal_lahir']
            agama= request.POST['agama']
            nohp= request.POST['nohp']
            nilai_un= request.FILES['nilai_un']
            nama_orangtua= request.POST['nama_orangtua']
            alamat_orangtua= request.POST['alamat_orangtua']
            nohp_orangtua= request.POST['nohp_orangtua']

            pendaftaran.objects.create(
                nama_depan=nama_depan,
                nama_belakang=nama_belakang,
                email=email,
                foto=foto,
                alamat=alamat,
                tempat_lahir=tempat_lahir,
                tanggal_lahir=tanggal_lahir,
                agama=agama,
                nohp=nohp,
                nilai_un=nilai_un,
                nama_orangtua=nama_orangtua,
                alamat_orangtua=alamat_orangtua,
                nohp_orangtua=nohp_orangtua,
            ).save()
            messages.success(request, "Berhasil Melakukan Pendaftaran Calon Siswa Baru")
            return HttpResponseRedirect('/')

    return render (request, 'pendaftaran.html',{'form':form})
