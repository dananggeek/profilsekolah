from django.shortcuts import render,get_object_or_404
from . models import *
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger

# Create your views here.
def index(request):
    about = About.objects.all()
    banner= Banner.objects.all()
    whyy= why.objects.all()
    
    return render (request,'profil/index.html',{'about':about,'banner':banner,'whyy':whyy})
