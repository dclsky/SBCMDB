#coding:utf-8
from models import Server,Users
from django.shortcuts import render_to_response,render
from forms import *
from PIL import Image  #pillow 图片处理
import hashlib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt #消除csrf
from django.http import HttpResponseRedirect

def get_md5(password):
    """
    密码加密
    :param password:
    :return:
    """
    md5 = hashlib.md5() #创建一个加密对象
    md5.update(password) #进行加密
    return md5.hexdigest() #返回加密结果

def serverlist(request):
    all_service = Server.objects.all()
    #all_s = Server.objects.raw("select * from server_server")
    return render_to_response("server_list.html",locals())

def register(request):
    regist = ServerForm()
    ourform = OurForm()
    return render_to_response("server_register.html",locals())

def service(request,id):
    #req = dir(request)
    req = request.META.items() #返回的是一个字典对象
    return render_to_response("service.html",locals())

def user_register(request):
    users = UserForm()
    if request.method == "POST":
        data = request.POST #用来接收我们post的数据
        img = request.FILES #用来接收image图片
        users = UserForm(data,img) #接收提交数据验证
        if users.is_valid(): #检测提交数据是否正常
            validData = users.cleaned_data #获取验证过的数据
            username = validData.get("username")
            password = validData.get("password")
            phone = validData.get("phone")
            email = validData.get("email")
            photo = validData.get("photo")

            #图片上传保存
            name = "static/img/"+photo.name #图像的名称
            img = Image.open(photo) #创建图片
            img.save(name) #进行保存，参数是保存的路径
            #数据库数据保存
            user = Users()
            user.username = username
            user.password = get_md5(password)
            user.phone = phone
            user.email = email
            user.photo = "img/"+photo.name
            user.save()
    else:
        user = UserForm()
    return render(request,"user_register.html",locals())

#@csrf_exempt
def save_Img(request):
    result = {"statue":"error","data":""}
    if request.method == "POST":
        #获取图片
        img = request.FILES
        photo = img.get("img")
        #保存图片
        name = "static/img/" + photo.name  # 图像的名称
        img = Image.open(photo)  # 创建图片
        img.save(name)  # 进行保存，参数是保存的路径
        #返回结果
        result["statue"] = "success"
        result["data"] = "/static/img/"+photo.name

    return JsonResponse(result)

def errors(request):
    return render_to_response("errors.html")




def login(request):
    result = {"statue":"error","data":""}
    if request.method == "POST" and request.POST:
        phone = request.POST["phone"]
        password = request.POST["password"]
        try:
            u = Users.objects.get(phone=phone)
        except Exception as e:
            result["data"] = "用户不存在"
        else:
            db_password = u.password
            send_password = get_md5(password)
            if db_password == send_password:
                response = HttpResponseRedirect("/index/")
                response.set_cookie("username",u.username,max_age=360)
                request.session["username"] = u.username
                return response
            else:
                result["data"] = "密码错误"
                return render(request,"login.html",locals())

    return render(request,"login.html",locals())

def uservalid(request):
    result = {"statue":"error","data":""}
    if request.method == "GET":
        try:
            phone = request.GET["phone"]
            u = Users.objects.get(phone = phone)
        except KeyError as e: #代表没有船phone
            result["data"] = "手机号不可为空"
        except: #取值错误
            result["data"] = "该手机号不存在"
        else:
            result["statue"] = "success"
            result["data"] = "ok"
    else:
        result["data"] = "请求错误"
    return JsonResponse(result)
# Create your views here.
