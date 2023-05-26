from django.contrib import admin
from django.urls import path
from std import views

urlpatterns = [
    path('std',views.index,name='stdhome'),
    path('register',views.register,name='reg'),
    path('login',views.login,name='login')
]
