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
from django.conf.urls import url,patterns
from django.contrib import admin
from qa.views import test
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', 'admin.site.urls'),
#     url(r'^ş', 'views.test', name='home'),
    url(r'^/$', 'test', name='home'),
    url(r'^login/.*$', 'test'),
    url(r'^signup/.*$', 'test'),
    url(r'^questions/\d+/$','test'),
    url(r'^ask/.*$', 'test'),
    url(r'^popular/.*$', 'test'),
    url(r'^new/.*$', 'test')
]
