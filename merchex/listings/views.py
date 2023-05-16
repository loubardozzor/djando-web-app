from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1> Hello Django</h1>')
def about(request):
    return HttpResponse('<h1>A propos</h1> <p> Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1> listings </h1>')

def contact(request):
    return HttpResponse('<h1>Contact-us</h1>')
