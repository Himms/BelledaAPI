from django.urls import path
from . import views

urlpatterns = [
    path('become-designer/', views.become_designer, name='become_designer')
]
