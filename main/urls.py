from django.urls import path
from main import views


app_name = 'main'


urlpatterns = [
        path('', views.index, name='index'),
        path('about-us/', views.about_us, name='about_us'),
        path('addresses/', views.addresses, name='addresses'),
]
