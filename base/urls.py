from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('room/', views.room, name="room"),
    path('footer/', views.footer, name="footer"),
    path('contact/', views.contact, name="contact"),
    path('products/', views.products, name = "products"),
    path('summary/', views.summary, name = "summary"),
    path('base/', views.base, name='base'),
    path('header/', views.header, name="header")
]