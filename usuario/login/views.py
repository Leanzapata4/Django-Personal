from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def iniciar (request):
    return render(request, "iniciar.html")

def registro (request):
    if request.method=="GET":
        return render(request, "registro.html",{"form": UserCreationForm})
    else: 
        if request.POST["password1"] != request.POST["password2"]:
            return render(request, "registro.html",{"form": UserCreationForm, "error": "Las contraseñas no coinciden"})
        else:
            name=request.POST["username"]
            password= request.POST["password1"]
            user= User.objects.create_user(username=name, password=password)
            user.save()
            return render(request, "registro.html",{"form": UserCreationForm, "error" : "Usuario registrado"} )