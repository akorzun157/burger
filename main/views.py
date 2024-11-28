from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Burger - Главная',
    }
    return render(request, 'main/index.html', context)


def about_us(request):
    context = {
        'title': 'Burger - О нас',
    }
    return render(request, 'main/about_us.html', context)


def addresses(request):
    context = {
        'title': 'Burger - Адреса',
    }
    return render(request, 'main/addresses.html', context)
