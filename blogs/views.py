from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def blog1(request):
   return render(request, 'blogs.html')
def blog2(request):
   return HttpResponse(" blog2 ")