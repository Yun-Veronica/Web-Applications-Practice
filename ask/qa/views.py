from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def test(request,*args, **kwargs):
    response_headers = [('Content-type','text/plain')]
    request_list= environ['QUERY_STRING'].split('&') 
    response_body = '42'.encode('utf-8')
    start_response('200 OK', response_headers)
    return HttpResponse('OK'), iter ([response_body])
