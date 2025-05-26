from django.shortcuts import render
from .models import Projectuser

def Projectusers(request):
    Project_user = Projectuser.objects.all()
    return render(request, 'usuarios/projectusers.html', {'projectusers': Project_user})

