from django.urls import path
from profil import views as views_post
app_name = 'profil'
urlpatterns= [
    path ('',views_post.index,name='index' ),
 
]
