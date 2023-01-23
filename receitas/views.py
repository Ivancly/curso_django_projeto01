from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('HOME')
    # return http response

def sobre(request):
    return HttpResponse('SOBRE')
    # return http response


def contato(request):
    return HttpResponse('CONTATO')
    # return http response

