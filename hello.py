# WSGI application return document with MIME type text/plain document, containing all GET parameters, one for each line.
# For example, when requesting "/?a=1&a=2&b=3", the application should return the following text:
# a=1
# a=2
# b=3


def wsgi_app(environ,start_response):
    status = "200 OK"
    response_headers = [('Content-type','text/plain')]
    request_list= environ['QUERY_STRING'].split('&') 
    response_body = ''
    for i in request_list:
        response_body += i+'\n'
    start_response(status, response_headers)
    return iter ([response_body.encode('utf-8')])

