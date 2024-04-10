from django.urls import path
from .views import add_to_wishlist, view_wishlist, remove_from_wishlist, toggle_wishlist
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('view/', view_wishlist, name='view_wishlist'),
    path('remove/<int:item_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/toggle/<int:product_id>/', toggle_wishlist, name='toggle_wishlist'),
]
    