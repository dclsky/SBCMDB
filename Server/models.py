#coding:utf-8
from django.db import models

class Server(models.Model):
    #python orm id默认有
    #python orm 字段默认不为空
    system = models.CharField(max_length = 32,verbose_name = "系统类型")
    ip = models.CharField(max_length = 32)
    mac = models.CharField(max_length = 32)
    controler = models.CharField(max_length = 32,verbose_name = "管理员")
    statue = models.CharField(max_length = 8,verbose_name = "状态")

class Users(models.Model):
    """
    设定用户需要头像
    登录以phone电话和密码
    """
    username = models.CharField(max_length = 32,verbose_name = "用户姓名")
    password = models.CharField(max_length = 32,verbose_name = "用户密码")
    phone = models.CharField(max_length = 32,verbose_name = "用户电话")
    email = models.EmailField(verbose_name = "用户邮箱",blank = True,null = True)
    photo = models.ImageField(upload_to = "img")
# Create your models here.
