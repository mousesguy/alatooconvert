from django.urls import path
from . import views

urlpatterns = [
    path('home',views.index, name = 'home'),
    path('aboutus', views.about, name = 'about'),
    path('master', views.master, name = 'master')

]