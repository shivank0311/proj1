from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,"index.html")

def myProfile(request):
    return HttpResponse("Welcome to my profile")