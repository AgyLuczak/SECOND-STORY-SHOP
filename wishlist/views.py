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
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, f'{product.name} added to your wishlist!')
    else:
        messages.error(request, f'{product.name} is already in your wishlist.')

    # Clear specific bag-related session variable if necessary
    request.session.pop('bag_action', None)

    return redirect('product_detail', product_id=product.id)
    
#The toggle action checks if an item is already in the wishlist, adding it if not, or removing it if present
@login_required
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)

    if created:
        request.session['wishlist_action'] = 'added'
        message = f'{product.name} added to your wishlist.'
    else:
        wishlist_item.delete()
        request.session['wishlist_action'] = 'removed'
        message = f'{product.name} removed from your wishlist.'

    context = {
        'wishlist_action': request.session.get('wishlist_action', 'No action'),
        'wishlist_items': WishlistItem.objects.filter(user=request.user)
    }

    request.session['wishlist_items'] = list(WishlistItem.objects.filter(user=request.user).values('product__name', 'product__image'))
    messages.success(request, message)
    return redirect(request.META.get('HTTP_REFERER', reverse('product_detail', args=[product.id])))
    
@login_required
def view_wishlist(request):
    # Assume you have a function to get wishlist items
    wishlist_items = WishlistItem.objects.filter(user=request.user).order_by('-added_on')
    product_count = len(wishlist_items)
    context = {
        'wishlist_items': wishlist_items,
        'product_count': product_count,
        'message': 'Your wishlist has been updated!',
    }
    return render(request, 'wishlist/wishlist.html', context)

@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
    wishlist_item.delete()
    messages.success(request, 'Item removed from your wishlist.',)
    return redirect('view_wishlist')