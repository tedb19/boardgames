from django.shortcuts import render


def home(request):
    template = "main/home.html"
    return render(request, template, locals())
