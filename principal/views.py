from django.shortcuts import render, HttpResponse

# Create your views here.

def Login(request):
    return render(request , 'login/loginPrincipal.html')

def yourname(request, name):
    return render(request , 'login/yourname.html', {'name': name})