from django.urls import path
from . import views

# import url paths here

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('zoo', views.zoo, name="zoo"),
    #path('book', views.book, name="book")
]