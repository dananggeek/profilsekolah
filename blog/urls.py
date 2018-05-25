from django.urls import path
from blog import views as blog
app_name = 'blog'
urlpatterns= [
    path ('',blog.index,name='index' ),
    path ('beritasekolah/<slug:slug>',blog.detail,name='detail' ),
]
