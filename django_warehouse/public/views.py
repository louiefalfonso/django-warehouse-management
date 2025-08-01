from django.shortcuts import render

def public(request):
    return render(request, "public/index.html")
