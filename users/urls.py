from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from users import views


app_name = 'users'


urlpatterns = [
        path('login/', views.login, name='login'),
]
