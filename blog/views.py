from django.shortcuts import render,get_object_or_404
from . models import *
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger

def index(request):
    post= Post.objects.order_by('-timupdate')

    #fungsi search
    qcari = request.GET.get("search")
    if qcari:
        post=post.filter(
            Q(title__icontains=qcari) |
            Q(content__icontains=qcari)

        ).distinct()

    #membuat paginations
    paginator = Paginator(post,3)
    page= request.GET.get('halaman')
    try:
        querypage= paginator.page(page)
    except PageNotAnInteger:
        querypage = paginator.page(1)
    except EmptyPage:
        querypage = paginator.page(paginator.num_pages)

    content = {
        "post":querypage,
    }
    return render (request,'blog/index.html',content)

def detail(request, slug):
    post=get_object_or_404(Post, slug=slug)
    return render (request,'blog/detail.html',{'post':post})
