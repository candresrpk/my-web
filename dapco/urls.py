from django.urls import path
from . import views

app_name = 'dapco'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.createEncuestView, name='create'),
]
