from django.shortcuts import render

from . models import *
# Create your views here.
def index(request):
    return render (request,'guru_siswa/index.html')
def guru(request):
    guru=Guru.objects.all()

    return render (request,'guru_siswa/data_guru.html',{'guru':guru})
def gurudetail(request, pk):

    detail= Guru.objects.get(id=pk)

    return render (request,'guru_siswa/data_guru_detail.html',{'detail':detail})
def siswa(request):
    siswa=Siswa.objects.all()
    return render (request,'guru_siswa/data_siswa.html',{'siswa':siswa})
def siswadetail(request ,pk):
    detail=Siswa.objects.get(id=pk)
    return render (request,'guru_siswa/data_siswa_detail.html',{'detail':detail})
def kelas(request):
    kelas=Kelas.objects.all()
    return render (request,'guru_siswa/data_kelas.html',{'kelas':kelas})
