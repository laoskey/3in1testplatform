from django.shortcuts import render ,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from apitest.models import Apitest, Apistep, Apis
from django.contrib.auth import authenticate,login


# Create your views here.


def home(request):
    return render(request,'home.html')


def test(request):
    return HttpResponse('Hello Python')


def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error':'username or password error.'})

    return render(request, 'login1.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login1.html')


#接口管理
@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all()  #读取所有流程接口数据
    username = request.session.get('user', '') # 读取浏览器登陆session
    return render(request, "apitest_manage.html", {'user': username,
                                                 'apitests': apitest_list
                                                 })#定义接口流程变量，并且返回前端

#接口流程步骤管理
@login_required
def apistep_manage(request):
    username = request.session.get('user', '')
    apistep_list = Apistep.objects.all()
    return render(request, "apistep_manage.html", {
        'user':username,
        'apisteps':apistep_list
    })


@login_required
def apis_manage(request):
    username = request.session.get('user', '')
    api_list = Apis.objects.all()
    return render(request, "apis_manage.html", {"user": username, "apiss": api_list})