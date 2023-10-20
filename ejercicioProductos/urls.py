"""
URL configuration for ejercicioProductos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import producto,detalles,detalles2,detalles3
from evaluacion2.views import vistaGeneral,vista1,vista2,vista3,vista4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', producto),
    path('electronica/', detalles),
    path('juguetes/', detalles2),
    path('ropa/', detalles3),

    path('', vistaGeneral),
    path('rubik1/',vista1),
    path('rubik2/',vista2),
    path('rubik3/',vista3),
    path('rubik4/',vista4)
]
