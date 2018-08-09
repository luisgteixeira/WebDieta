from django.shortcuts import render

def dieta(request):
    return render(request, 'dieta/dieta.html')

def dashboard(request):
    return render(request, 'dieta/dashboard.html')
