from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import PostModel
# Create your views here.


def redir_top(request):
    return redirect('/top/')


def top(request):
    return render(request, 'top.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = email.split('@')[0]
        password = request.POST['password']
        try:
            User.objects.create_user(username=username, email=email, password=password)
            can_login = authenticate(request, username=username, password=password)
            login(request, can_login)
            return redirect('alltweet')
        except:
            return render(request, 'signin.html', {'error': '登録済みユーザーです'})

    return render(request, 'signin.html')


def mylogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = email.split('@')[0]
        password = request.POST['password']
        can_login = authenticate(request, username=username, password=password)
        print(can_login)
        if can_login:
            login(request, can_login)
            return redirect('mypage')
        else:
            try:
                User.objects.get(username=username)
                return render(request, 'login.html', {'error': 'パスワードが違います'})
            except:
                return render(request, 'login.html', {'error': '登録されていないユーザーです'})
    return render(request, 'login.html')


@login_required
def alltweet(request):
    objects_list = PostModel.objects.all().order_by('-date')
    return render(request, 'alltweet.html', {'objects_list': objects_list})


@login_required
def mypage(request):
    username = request.user
    try:
        objects_list = PostModel.objects.filter(post_name=username).order_by('-id')

    except:
        objects_list = []

    if request.method == 'POST':
        if request.POST['context'] == '':
            return redirect('mypage')
        new_post = PostModel(post_name=username, context=request.POST['context'])
        new_post.save()
        return redirect('mypage')

    return render(request, 'mypage.html',
                  {'username': username, 'objects_list': objects_list})


@login_required
def log_out(request):
    logout(request)
    return redirect('top')


@login_required
def delete(request, pk):
    PostModel.objects.filter(id=pk).delete()
    return redirect('mypage')


@login_required
def other(request, name):
    objects_list = PostModel.objects.filter(post_name=name).order_by('-id')
    return render(request, 'other.html',
                  {'username': name, 'objects_list': objects_list})