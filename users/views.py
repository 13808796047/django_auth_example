from django.shortcuts import render, redirect
from . import forms


def register(request):
    # 从get或者post请求中获取next参数值
    # get请求中，next通过url传递，即/?next=value
    # post请求中，next通过表单传递，即<input type='hidden' name='next' value="{{next}}"
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    # 只有当请求为POST时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST是一个类字典数据结构，记录了用户提交的注册信息
        # 这是提交的就是用户名(username)、密码(password)、邮箱(email)
        # 用这些数据实例化一个用户注册表单
        form = forms.RegisterForm(request.POST)
        # 验证数据的合法性
        if form.is_valid():
            # 如果提交的数据合法，调用表单的save方法将用户数据保存到数据库
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                # 注册成功，跳转回首页
                return redirect('/')
    else:
        # 请求不是POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = forms.RegisterForm()
    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'users/register.html', {'form': form, 'next': redirect_to})


def index(request):
    return render(request, 'index.html')
