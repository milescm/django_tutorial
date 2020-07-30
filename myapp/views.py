from django.shortcuts import render, redirect
import random
from .models import Post

# def post_list(request):
    # return render(request, 'myapp/post_list.html', {})

def index_list(request):
    return render(request, 'myapp/index_list.html', {})


def dinner(request):
    menu = ["Jockbal", "Hanbur", "Chicken", "Sushi"]
    pick = random.choice(menu)
    return render(request, 'myapp/dinner.html', {'dinner': pick})

def hello(request, name):
    return render(request, 'myapp/hello.html', {'name': name})

def throw(request):
    return render(request, 'myapp/throw.html')

def catch(request):
    message = request.GET.get('message')
    return render(request, 'myapp/catch.html', {'message': message})

def naver(request):
    return render(request, 'myapp/naver.html')


# CRUD - model.Post

def new(request):
    return render(request, 'myapp/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    post = Post(title=title, content=content)
    post.save()

    return redirect(f'{post.pk}/')

def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'myapp/detail.html', {'post': post})

def post_list(request):
    post = Post.objects.all()
    return render(request, 'myapp/post_list.html', {'post': post})

