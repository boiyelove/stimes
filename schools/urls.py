from django.conf.urls import url
from . import views as school_views


urlpattern = [
	url(r'^$', school_views.school_home, name='school_home'),
	]