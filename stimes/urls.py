"""stimes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from schools import views

urlpatterns = [
    url(r' ^autocomplete/' , include('autocomplete_light.urls' )),
    url(r'^accounts/', include('accounts.urls', namespace='accoounts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/add', views.create_article, name = 'create_article'),
    url(r'^schools/add', views.create_school, name = 'create_school'),
    url(r'^lecture/add', views.create_lecture, name = 'create_lecture'),
    url(r'^event/add', views.create_event, name = 'create_event'),
    url(r'^testtemplate/$', views.test_template, name='test_template'),
        ]
