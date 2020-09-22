"""qatrosnico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from sample import views as sample
from sample.views import APIItems, ItemCreate,DetailViews,ItemUpdate,ItemDelete

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', sample.home, name='index'),
    path('documentation/', sample.documentation, name='documentation'),
    path('api/', APIItems.as_view(), name='api'),
    path('api/<int:pk>/', APIItems.as_view(), name='api'),

    path('create/', sample.ItemCreate, name='create'),
    path('detail/<int:pk>/', DetailViews.as_view(), name='detail'),
    path('delete/<int:pk>/', ItemDelete.as_view(), name='delete'),
    path('update/<int:pk>/', ItemUpdate.as_view(), name='update'),
    # path('', include('sample.urls' , namespace='sample'))
]
