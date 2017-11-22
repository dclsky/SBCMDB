#coding:utf-8
from django import forms
from models import Server

class OurForm(forms.Form):
    system = forms.CharField(
        max_length = 32,
        label = "系统类型",
        widget = forms.TextInput(attrs={"class":"form-control","placeholder":"系统类型"})
        )
    ip = forms.CharField(
        max_length = 32,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "ip"})
    )
    mac = forms.CharField(
        max_length = 32,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "mac"})
    )
    controler = forms.CharField(
        max_length = 32,
        label = "管理员",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "管理员"})
    )
    statue = forms.CharField(
        max_length = 8,
        label = "状态",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "状态"})
    )
    choice = forms.ChoiceField(
        choices = Server.objects.values_list("id","system")
        # choices = (
        #     (0,"1"),
        #     (1,"2"),
        #     (3,"3")
        # )
    )

class ServerForm(forms.ModelForm):
    class Meta: #元类
        model = Server #对应的模型
        fields = ("system","ip","mac","controler","statue") #需要生成的字段

class UserForm(forms.Form):
    username = forms.CharField(
        max_length = 32,
        label = "用户姓名",
        widget = forms.TextInput(attrs={"class": "form-control", "placeholder": "用户姓名"})
    )
    password = forms.CharField(
        max_length = 32,
        label = "用户密码",
        widget = forms.TextInput(attrs={"class": "form-control", "placeholder": "用户密码"})
    )
    phone = forms.CharField(
        max_length = 32,
        label = "用户电话",
        widget = forms.TextInput(attrs={"class": "form-control", "placeholder": "用户电话"})
    )
    email = forms.EmailField(
        required = False,
        label = "用户邮箱",
        widget = forms.TextInput(attrs={"class": "form-control", "placeholder": "用户邮箱"})
    )
    photo = forms.ImageField(
        max_length = 8,
        label = "用户头像",
        widget = forms.FileInput(attrs={"class": "form-control", "placeholder": "用户头像"})
    )