from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('become-designer/', views.become_designer, name='become_designer'),
    path('designer-admin/', views.designer_admin, name='designer_admin'),
    path('add-design/', views.add_design, name='add_design'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
