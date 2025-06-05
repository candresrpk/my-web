from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.Signup, name='signup'),
    path('signin/', views.Signin, name='signin'),
]