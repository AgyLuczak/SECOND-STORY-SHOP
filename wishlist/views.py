from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WishlistItem
from products.models import Product
from django.db.models import Value, BooleanField

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    WishlistItem.objects.get_or_create(user=request.user, product=product)
    messages.success(request, 'Product added to your wishlist!',)
    return redirect('product_detail', product_id=product.id) 

#The toggle action checks if an item is already in the wishlist, adding it if not, or removing it if present
@login_required
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)

    if created:
        message = f'{product.name} added to your wishlist.'
    else:
        wishlist_item.delete()
        message = f'{product.name} removed from your wishlist.'

    messages.success(request, message)
    return redirect(request.META.get('HTTP_REFERER', reverse('product_detail', args=[product.id])))


@login_required
def view_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user).order_by('-added_on')
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'wishlist/wishlist.html', context)


@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
    wishlist_item.delete()
    messages.success(request, 'Item removed from your wishlist.',)
    return redirect('view_wishlist')