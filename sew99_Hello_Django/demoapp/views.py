from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_demo(request):
    return HttpResponse("<h1> Hello Django!</h1>")

