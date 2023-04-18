from django.shortcuts import render

def uno(request):
    return render(request, "template.html")
