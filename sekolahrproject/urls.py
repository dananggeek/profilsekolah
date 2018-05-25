"""sekolahrproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from blog import views as blog

from profil import views as views_post
from guru_siswa import views as views_guru_siswa
from daftarsiswa import views as views_pendaftaran
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path ('admin/', admin.site.urls),
    #blog
    path('', include('blog.urls', namespace='blogs')),
    #profil
    path('', include('profil.urls', namespace='profils')),
    #pendaftara
    path ('pendaftaran/',views_pendaftaran.add,name='add' ),
    #Calender
    path('', include('calender.urls', namespace='calenders')),
    #gutusiswa
    path ('gurusiswa/',views_guru_siswa.index,name='index' ),
    path ('gurusiswa/guru/',views_guru_siswa.guru,name='guru' ),
    path ('gurusiswa/guru/detail/<int:pk>',views_guru_siswa.gurudetail,name='gurudetail' ),
    path ('gurusiswa/siswa/',views_guru_siswa.siswa,name='siswa' ),
    path ('gurusiswa/siswa/detail/<int:pk>',views_guru_siswa.siswadetail,name='siswadetail' ),
    path ('gurusiswa/kelas/',views_guru_siswa.kelas,name='kelas' ),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
