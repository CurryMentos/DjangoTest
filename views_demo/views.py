import ast
import json
import random

from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.views import View

# def hello_world(request):
#     print("请求文件路径" + request.path)
#     print("请求方法" + request.method)
#     print("请求正文信息" + str(request.body))
#     print("get请求数据" + str(request.GET.dict()))
#     print("post请求数据" + str(request.POST.dict()))
#     print("cookie信息" + str(request.COOKIES))
#     print("文件上传数据" + str(request.FILES))
#     return render(request, "test.html", {"name": "曾佑祖"})
#
#
# def test_redirect(request):
#     # return redirect(hello_world)
#     return JsonResponse([{"code": 2000, "msg": "成功"}], safe=False) #数据类型为列表,必须制定safe=False;字典不必指定


# class Projects(View):
# def get(self,request,pk):
#     print(pk)
#     return HttpResponse("查询了一个项目")
# def post(self,request,pk):
#     return HttpResponse("新增了一个项目")
# def put(self,request,pk):
#     return HttpResponse("修改了一个项目")
# def delete(self,request,pk):
#     return HttpResponse("删除了一个项目")

# def login(request):
#     dict = request.GET.dict()
#     userName = dict['userName']
#     password = dict['password']
#
#     with open("views_demo/login.txt", "r", encoding="utf-8")as file:
#         list = [i for i in file.readlines()]
#         s = str(list).replace("[", "").replace("]", "").replace("'", "")
#         newDict = json.loads(s)
#
#         if (userName == newDict['userName'] and password == newDict['password']):
#             return HttpResponse("登录成功")
#         else:
#             return HttpResponse("登录失败")

# def phone(request):
#     second = [3, 4, 5, 7, 8][random.randint(0, 4)]
#     phone = str(1) + str(second) + "".join(random.choice("0123456789") for i in range(9))
#     return HttpResponse(phone)

from model_demo.models import Student


class Projects(View):
    @transaction.atomic
    def get(self, request):
        students = Student.objects.filter(s_name__startswith="小").order_by('id')
        student_list = []
        for s in students:
            dict = {
                "id": s.id,
                "name": s.s_name,
                "sex": s.s_sex,
                "phone": s.s_phone,
                "creat_time": s.create_time,
                "update_time": s.update_time,
            }
            student_list.append(dict)
            p = Paginator(student_list, per_page=10)
        # return JsonResponse({"code": "123213", "message": "成功", "data": None}, safe=False)
        return JsonResponse(p.get_page(1).object_list, safe=False)

    @transaction.atomic
    def post(self, request):
        student = json.loads(request.body)
        student_list = [Student(s_name=s["name"], s_sex=s["sex"], s_phone=s["phone"]) for s in student]
        Student.objects.bulk_create(student_list)
        return JsonResponse({"code": "123213", "message": "成功", "data": None}, safe=False)

    @transaction.atomic
    def put(self, request):
        data = json.loads(request.body)
        students = Student.objects.filter(id=data["id"])
        students.update(**data)
        return JsonResponse({"code": "123213", "message": "成功", "data": data}, safe=False)

    @transaction.atomic
    def delete(self, request):
        data = json.loads(request.body)
        Student.objects.filter(id=data["id"]).delete()
        # Student.objects.all().delete()
        return JsonResponse({"code": "123213", "message": "成功", "data": data}, safe=False)
