from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):

    char = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))


    if request.GET.get('special'):
        char.extend(list('!@#$%^&*_+-'))

    if request.GET.get('num'):
        char.extend(list('1234567890'))

    len = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(len):
        thepassword += random.choice(char)

    return render(request, 'generator/password.html', {'password':thepassword})

