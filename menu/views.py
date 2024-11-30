from django.shortcuts import render

from menu.models import Products

# Create your views here.
def menu(request):

    menu = Products.objects.all()

    context = {
        'title': 'Burger - Меню',
        'menu': menu,
    }
    return render(request, 'menu/menu.html', context)