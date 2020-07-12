from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

# Create your views here.
from django.views import View


class Login(View):
    def get(self, request):
        response = HttpResponse()
        response.set_cookie("JSessionId", "yegqlqx9f!f", max_age=120)
        response.content = "ok"
        return response

    def post(self, request):
        print(request.COOKIES)
        return HttpResponse("ok")

    def put(self,request):
        cookie = request.COOKIES
        request.session["zyz"] = cookie["JSessionId"]
        return HttpResponse("ok")

def signup(request):
    '''用户注册方法'''
    data = json.loads(request.body)
    user = User.objects.create_user(username=data['username'],password=data['password'],email=data['email']) # 使用User模块的create_user方法创建用户
    user.save()
    info = {
        "code":'0000',
        'msg':"用户注册成功",
        'data':{
            "id":user.id,
            "username":user.username,
            "password":user.password
        }
    }
    return JsonResponse(info) # 使用JsonResponse返回一个json字符串

def user_login(request):
    '''
    用户登录方法
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return HttpResponse("登录页面")
    data = json.loads(request.body)
    user = authenticate(username=data["username"], password=data["password"])
    info = {
        "code":None,
        'msg':None
    }
    if user is not None:
        if user.is_active:
            login(request,user) # 调用django.contrib.auth模块的login
            info["code"] = "0000"
            info["msg"] = "登录成功"
        else:
            info["code"] = "9999"
            info["msg"] = "该账户不可用"
    else:
        info["code"] = "9999"
        info["msg"] = "用户名密码不正确"
    return JsonResponse(info)

def user_logout(request):
    '''退出登录'''
    logout(request) # 调用django.contrib.auth模块的logout方法
    info = {
        "code": "0000",
        'msg': "退出登录成功"
    }
    return JsonResponse(info)

def test(request):
    return HttpResponse("登录页面")

@login_required(login_url='/login/test1')# 此装饰器会校验会在访问该视图之前，校验session，若通过则继续，不通过则重定向到login_url指定的视图中去
def test_user(request):
    '''
    测试登录
    :param request:
    :return:
    '''
    return HttpResponse('ok')