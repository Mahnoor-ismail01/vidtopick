import imp
from django.urls import path
from .views import *
urlpatterns = [
    path('uploadlink/', uploadlink, name='uploadlink'),
]
