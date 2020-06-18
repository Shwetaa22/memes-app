import random

import requests
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse, response
from django.shortcuts import render, redirect

# Create your views here.
from django.template import RequestContext
from django.urls import reverse

from .models import UserProfile


def homeView(request):
    print('sd')
    res = requests.get("https://api.imgflip.com/get_memes")
    res_json = res.json()
    data = res_json['data']['memes']
    # print(data)
    meme_dict = random.sample([ sub['url'] for sub in data ] ,5) #dict(random.sample(list(res_json.items()), 5))
    return render(request, 'home.html',{'meme_dict':meme_dict})


def login_request(request):
    print('s')
    form = AuthenticationForm()
    return render(request, "login.html", context={"form": form})


def user_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)

                response = redirect('home')
                response.set_cookie('user_info', 'Hello ' + user.username + '!!...You are logged in now.')
                return response
                # return render(request, 'home.html', {})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return render(request, 'home.html', {})
    else:
        return render(request, 'login.html', {})


def user_data(request):
    id = request.POST.get('id')
    flag = request.POST.get('flag')
    UserProfile.objects.update_or_create(user_id=id, defaults={'is_accpted': flag})
    return HttpResponse("stored")


def logout_request(request):
    logout(request)
    response = redirect('home')
    response.delete_cookie('user_info')
    # response.set_cookie('user_info', '')
    return response
