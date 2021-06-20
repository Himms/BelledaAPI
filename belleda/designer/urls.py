from django.urls import path
from . import views

urlpatterns = [
    path('become-designer/', views.become_designer, name='become_designer'),
    path('designer-admin/', views.designer_admin, name='designer_admin')
]
