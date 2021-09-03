"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from blog import views                    #+
from .views import login,index,main,jquery
urlpatterns = [
    # path('index', views.hello)   ,       #+
    path('admin/', admin.site.urls),
    path('login',login),
    path('index',index),
    path('main',main),
    path('static/libs/jquery.js',jquery),
]

# 增加条目
# handler400=views.bad_request
# handler403=views.permission_denied
# handler404=views.page_not_found
# handler500=views.page_error







