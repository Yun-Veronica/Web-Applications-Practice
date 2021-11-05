from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def test(request,*args, **kwargs):
    response_body = 'Answer is 42'.encode('utf-8')
    start_response('200 OK',  [('Content-type','text/plain')])
    return  iter ([response_body]), HttpResponse('OK')
