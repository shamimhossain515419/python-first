from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
  return HttpResponse("Welcome")  

def contact(request):
  return HttpResponse("Welcome contact me")  

