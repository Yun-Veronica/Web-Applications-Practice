# WSGI application return document with MIME type text/plain document, containing all GET parameters, one for each line.
# For example, when requesting "/?a=1&a=2&b=3", the application should return the following text:
# a=1
# a=2
# b=3


def wsgi_app(environ,start_response):
    status = "200 OK"
    response_headers = [('Content-type','text/plain')]
    response_body = [ (bytes(i, 'ascii') + b'\n') for i in environ['QUERY_STRING'].split('&') ]
    start_response(status, response_headers)
    return [response_body]

