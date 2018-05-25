from django.shortcuts import render , get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
# Create your views here.

def index(request):
    list = Calender.objects.order_by('-id')
    #search
    qcari = request.GET.get("search")
    if qcari:
            list=list.filter(
                Q(judul__icontains=qcari) |
                Q(lokasi__icontains=qcari) |
                Q(deskripsi__icontains=qcari)
            ).distinct()
    #paghinations
    paginator = Paginator(list,15)
    page = request.GET.get('halaman')
    try:
        querylist = paginator.page(page)
    except PageNotAnInteger:
        querylist = paginator.page(1)
    except EmptyPage:
        querylist = paginator.page(paginator.num_pages)

    list_content = {"list":querylist,}
    return render (request ,'calender/index.html',list_content)

def detail(request ,slug):
    detail = get_object_or_404(Calender, slug=slug)
    return render (request ,'calender/detail.html',{'detail':detail})
