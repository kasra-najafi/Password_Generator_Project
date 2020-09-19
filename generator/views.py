from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')



def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppers = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    specials = list('!@#$%^&*()_+-=.,/?;:|`~')

    length = int(request.GET.get('length', 2))

    if request.GET.get('uppercase'):
        characters.extend(uppers)

    if request.GET.get('numbers'):
        characters.extend(numbers)

    if request.GET.get('special'):
        characters.extend(specials)

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')