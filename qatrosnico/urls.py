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
from sample2 import views as sample2
from sample.views import APIItems,ItemDetailViews,ItemUpdate,ItemDelete
from sample2.views import BusDetailViews, ScheduleDetailViews, StationDetailViews, BusUpdate, BusDelete, ScheduleUpdate, ScheduleDelete, StationUpdate, StationDelete
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', sample.home, name='home'),

    #Tugas 2
    path('sample2/', sample2.index, name='index2'),
    path('documentation2/', sample2.documentation, name='documentation2'),

    path('create_bus/', sample2.BusCreate, name='create_bus'),
    path('create_schedule/', sample2.ScheduleCreate, name='create_schedule'),
    path('create_station/', sample2.StationCreate, name='create_station'),

    path('detail_bus/<int:pk>/', BusDetailViews.as_view(), name='detail_bus'),
    path('detail_schedule/<int:pk>/', ScheduleDetailViews.as_view(), name='detail_schedule'),
    path('detail_station/<int:pk>/', StationDetailViews.as_view(), name='detail_station'),

    path('update_bus/<int:pk>/', BusUpdate.as_view(), name='update_bus'),
    path('update_schedule/<int:pk>/', ScheduleUpdate.as_view(), name='update_schedule'),
    path('update_station/<int:pk>/', StationUpdate.as_view(), name='update_station'),

    path('delete_bus/<int:pk>/', BusDelete.as_view(), name='delete_bus'),
    path('delete_schedule/<int:pk>/', ScheduleDelete.as_view(), name='delete_schedule'),
    path('delete_station/<int:pk>/', StationDelete.as_view(), name='delete_station'),

    #Tugas 1
    path('sample1/', sample.index, name='index'),
    path('documentation/', sample.documentation, name='documentation'),
    path('api/', APIItems.as_view(), name='api'),
    path('api/<int:pk>/', APIItems.as_view(), name='api'),

    path('create/', sample.ItemCreate, name='create_item'),
    path('detail/<int:pk>/', ItemDetailViews.as_view(), name='detail_item'),
    path('delete/<int:pk>/', ItemDelete.as_view(), name='delete_item'),
    path('update/<int:pk>/', ItemUpdate.as_view(), name='update_item'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

