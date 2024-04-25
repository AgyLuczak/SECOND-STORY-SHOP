from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
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
    # return redirect('product_detail', product_id=product.id)
    redirect_url = request.META.get('HTTP_REFERER', 'default_fallback_url')  # Fallback URL if HTTP_REFERER is not available
    return HttpResponseRedirect(redirect_url)
    
# The toggle action checks if an item is already in the wishlist, adding it if not, or removing it if present
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
    messages.success(request, message)
    request.session.modified = True  
    # return redirect(reverse('view_wishlist')) 
    

    # Redirect the user to the URL specified in the 'next' parameter or to a default view
    next_page = request.GET.get('next', reverse('view_wishlist'))
    return redirect(next_page)

@login_required
def view_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user).order_by('-added_on')
    product_count = len(wishlist_items)
    message = None
    if 'wishlist_action' in request.session:
        action = request.session.pop('wishlist_action', None)
        message = f'Item {action} your wishlist.'  
        request.session.modified = True
    context = {
        'wishlist_items': wishlist_items,
        'product_count': product_count,
        'message': message,
    }
    return render(request, 'wishlist/wishlist.html', context)
    
@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
    wishlist_item.delete()
    messages.success(request, 'Item removed from your wishlist.',)
    return redirect('view_wishlist')
@login_required
def clear_wishlist_action(request):
    if 'wishlist_action' in request.session:
        del request.session['wishlist_action']
    return HttpResponse('OK')