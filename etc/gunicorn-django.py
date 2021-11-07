CONFIG = {                                                                                                  
    'mode': 'wsgi',                                                                                      
    'working_dir': '/home/box/web/ask',                                                                      
    # 'python': '/usr/bin/python',                                                                          
    'args': (                                                                                              
        '--bind=0.0.0.0:8000',
  '--daemon',
  '--access-logfile=gunicorn.access.log',
  '--error-logfile=gunicorn.error.log',
  '--log-level=info',
        'ask.wsgi:application',                                                                                      
    ),                                                                                                      
}
