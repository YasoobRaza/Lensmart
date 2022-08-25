from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("login", views.loginUser, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("signup", views.signup, name="signup"),
    path("products", views.products, name="products"),
    path("cart", views.cart, name="cart"),
    path("order", views.order, name="order") 
]