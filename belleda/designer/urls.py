from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('become-designer/', views.become_designer, name='become_designer'),
    path('designer-admin/', views.designer_admin, name='designer_admin'),
    path('logout/', auth_views.LogoutView.as_view, name='logout'),
]
