from django.http.response import HttpResponse
from django.http import HttpResponse
# Create your views here.

def home(response):
    return HttpResponse('Hi there')