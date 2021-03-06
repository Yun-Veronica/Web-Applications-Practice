"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from qa import views

# custom 404 error
# handler404 = 'qa.views.handler404'

urlpatterns = [
    url('404', views.handler404),
    url(r'^ /?page=\d+/$', views.main_page, name='main_page'),
    url(r'^login/.*$', views.test),
    url(r'^signup/.*$', views.test),
    url(r'^questions/\d+/$', views.question_page),
    url(r'^ask/.*$', views.test),
    url(r'^popular/\d+/.*$', views.popular_pages),
    url(r'^new/.*$', views.test)
]
