from django.urls import path

from django.contrib import admin
from django.urls import URLPattern, path, include

urlpaterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

from .views import funcionario, index, agenda, cliente, login, listaprecos

urlpatterns = [
    path('', index),
    path('agenda', agenda),
    path('cliente', cliente),
    path('funcionario', funcionario),
    path('login', login),
    path('listaprecos', listaprecos),
]