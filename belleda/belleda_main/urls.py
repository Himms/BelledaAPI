from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('nav_item/', views.nav_item, name='nav_item'),
]
