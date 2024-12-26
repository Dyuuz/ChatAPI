from ChatSystem.urls import path
from .views import *
from Api import views

urlpatterns = [
    path('', views.home , name="home"),
    path('api/register', UserRegistration.as_view(), name="user-register"),
    path('api/login', UserLogin.as_view(), name="user-login"),
    path('api/chat', ChatAPI.as_view(), name="chat-api"),
    path('api/balance', Balance.as_view(), name="balance"),
]
