from django.urls import path
from . import views

app_name = 'sato'
urlpatterns = [
    path('', views.index, name='index'),
]
