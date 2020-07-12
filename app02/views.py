import json

from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from utils.token import create_token
from utils.token import delete_token

# Create your views here.
from django.urls import reverse
from django.views import View


def auth(request):
    return HttpResponse("认证成功")


class Signup(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get("username", None)
        password = data.get("password", None)
        email = data.get("email", None)
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            token = create_token(user.username)
            return JsonResponse({"code": "0000", "msg": "注册成功", "data": token})
        except:
            return JsonResponse({"code": "9999", "msg": "注册失败", "data": None})


class Login(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)
        if user:
            token = create_token(user.username)
            return JsonResponse({"code": "0000", "msg": "登录成功", "data": token})
        else:
            return JsonResponse({"code": "9999", "msg": "账号或密码错误", "data": None})


class Logout(View):
    def post(self, request):
        delete_token(request.META.get("HTTP_TOKEN"))
        return JsonResponse({"code": "0000", "msg": "退出登录成功", "data": None})


class UpdatePassword(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get("username", None)
        origin_password = data.get("origin_password", None)
        update_password = data.get("update_password", None)
        re_update_password = data.get("re_update_password", None)
        user = User.objects.filter(username=username).first()
        if origin_password == update_password:
            return JsonResponse({"code": "9999", "msg": "新密码不能与旧密码一致", "data": None})
        elif update_password != re_update_password:
            return JsonResponse({"code": "9999", "msg": "两次密码输入不一致", "data": None})
        else:
            user.set_password(update_password)
            user.save()
            return JsonResponse({"code": "0000", "msg": "修改密码成功", "data": None})