from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.mainvid, name='mainvid'),
    #path('auth/', views.mainvid, name='mainvid'),
    path('alogin/', views.afterlogin, name='afterlogin'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('history/', views.history, name='history'),
    path('favorites/', views.favorites, name='favorites'),
    path('login/', auth_view.LoginView.as_view(template_name='authentication/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='authentication/logout.html'), name="logout"),
]