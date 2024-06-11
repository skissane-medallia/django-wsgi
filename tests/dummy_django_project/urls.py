from django.conf.urls import re_path
from django.http import HttpResponse


urlpatterns = [
    re_path('^$', lambda request: HttpResponse()),
]
