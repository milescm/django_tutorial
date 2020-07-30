from django.shortcuts import render
import random

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