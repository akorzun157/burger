from django.shortcuts import get_object_or_404, render

from menu.models import Categories, Products

# Create your views here.
def menu(request, category_slug=None):
    
    menu = Products.objects.all() 
    categories = Categories.objects.all()  

    if category_slug == 'all' or category_slug is None:
        menu = Products.objects.all() 
    else:
        category = get_object_or_404(Categories, slug=category_slug)
        menu = Products.objects.filter(category=category)

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