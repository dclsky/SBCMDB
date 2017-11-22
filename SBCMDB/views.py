#coding:utf-8
from Server.models import *
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect

def loginValid(fun):
    def inner(request,*args,**kwargs):
        username = request.session.get("username")
        # cookie = request.COOKIES.get("username")
        if username:
            fun(request)
        else:
            return HttpResponseRedirect("/server/login/")
    return inner()

@loginValid
def index(request):
    u = Users.objects.get(id=6)
    return render_to_response("index.html",locals())
# def index(request):
#     username = request.session.get("username")
#     cookie = request.COOKIES.get("username")
#     if username:
#         u = Users.objects.get(id = 6)
#         return render_to_response("index.html",locals())
#     else:
#         return HttpResponseRedirect("/server/login/")

def server_list(request):
    return render_to_response("server_list.html",locals())