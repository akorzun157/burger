from django.shortcuts import render

from menu.models import Categories, Products

# Create your views here.
def menu(request):

    menu = Products.objects.all()
    categories = Categories.objects.all()

    context = {
        'title': 'Burger - Меню',
        'menu': menu,
        'categories': categories,
    }
    return render(request, 'menu/menu.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {"product": product}

    return render(request, 'menu/product.html', context)