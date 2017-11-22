from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^list/', serverlist),
    url(r'^service/(\d{1,3})',service),
    url(r'^register/', register),
    url(r'^user_register/', user_register),
    url(r'^save_Img/', save_Img),
    url(r'^error/', errors),
    url(r'^login/', login),
    url(r'^uservalid/', uservalid),
]
