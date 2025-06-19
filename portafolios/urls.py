from django.urls import path
from . import views


app_name = 'portafolios'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.createView, name='create'),
]