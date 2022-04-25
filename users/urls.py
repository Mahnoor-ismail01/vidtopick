import imp
from django.urls import path
from .views import *
urlpatterns = [
    path('auth/', display_view, name='auth'),
    path('logout/', logout_view, name='logout'),
]
