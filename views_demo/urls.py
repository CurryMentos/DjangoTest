"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('helloworld/', views.hello_world),
    # path('h/', views.test_redirect),
    # path("projects/<int:pk>",views.Projects.as_view(),{"pk":"123"}),
    # re_path(r"^projects/(?P<pk>[\d]+).?$",views.Projects.as_view()),
    # path('login/',views.login),
    # path('phone/',views.phone),
    path('projects/', views.Projects.as_view()),
]
