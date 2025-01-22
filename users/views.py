from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'Burger - Авторизация',
    }
    return render(request, 'users/login.html',  context)


def registration(request):
    context = {
        'title': 'Burger - Регистрация',
    }
    return render(request, 'users/registration.html',  context)