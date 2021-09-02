from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def   hello(request):
      return HttpResponse('Hello World')



def   page_not_found(request):
      return render(request,'404.html')

def   page_error(request):
      return render(request,'500.html')

def   permission_denied(request):
      return render(request,'403.html')

def   bad_request(request):
      return render(request,'400.html')