from django.urls import path
from .views import ParkingHostCreate
from . import views

app_name = 'parking_req'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', ParkingHostCreate.as_view(), name='create')
]