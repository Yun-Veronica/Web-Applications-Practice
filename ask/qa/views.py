from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def test(request,*args, **kwargs):
    #response_body = b'Answer is 42'.encode('utf-8')
    return HttpResponse('Answer is 42', headers={ 'Content-Type': 'text/plain', 'status_code':200})
