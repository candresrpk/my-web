from django.shortcuts import render

# Create your views here.
def Signup(request):
    return render(request, 'users/signup.html')


def Signin(request):
    return render(request, 'users/signin.html')