from django.urls import path
from .views import ListCategory, DetailCategory, ListDesign, DetailDesign, ListUser, DetailUser, ListCart, DetailCart
urlpatterns = [
    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),

    path('designs', ListDesign.as_view(), name='designs'),
    path('designs/<int:pk>/', DetailDesign.as_view(), name='singledesign'),

    path('users', ListUser.as_view(), name='users'),
    path('users/<int:pk>/', DetailUser.as_view(), name='singleuser'),

    path('carts', ListCart.as_view(), name='allcarts'),
    path('carts/<int:pk>', DetailCart.as_view(), name='cartdetail'),
]
