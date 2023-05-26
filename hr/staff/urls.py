from django.contrib import admin
from django.urls import path,include
from staff import views

urlpatterns = [
    path('',views.index,name='home'),
    path('staff',views.index,name='home'),
    path('hrlogin',views.hrlogin,name='hrlogin'),
    path('mock',views.mock,name='mock')
]