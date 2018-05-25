from django.urls import path
from calender import views as views_calender
app_name = 'calender'
urlpatterns= [
    path ('calender/',views_calender.index,name='index' ),
    path ('calender/detail/<slug:slug>',views_calender.detail,name='detail' ),
]
