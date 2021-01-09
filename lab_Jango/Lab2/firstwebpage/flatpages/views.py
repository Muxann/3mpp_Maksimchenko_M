from django.shortcuts import render
from django.http import HttpResponse
from django import template
def home(request):
    return render(request, 'templates/static_handler.html')
#def home(request):
    #return HttpResponse(u'Привет, Мир!!', content_type="text/plain")
def hello(request):
    return HttpResponse(u'Привет, Мир!!')
# Create your views here.
