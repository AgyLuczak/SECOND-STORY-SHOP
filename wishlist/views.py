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
    """Add a product to the user's wishlist."""
    # Retrieve the product by ID, or return a 404 error if not found
    product = get_object_or_404(Product, id=product_id)
    # Get or create a WishlistItem for the product and the user
    wishlist_item, created = WishlistItem.objects.get_or_create(
        user=request.user, product=product
    )
    if created:
        # If the WishlistItem was newly created, add a success message
        messages.success(request, f"{product.name} added to your wishlist!")
    else:
        # If the WishlistItem already exists, add an error message
        messages.error(request, f"{product.name} is already in your wishlist.")
    # Clear specific bag-related session variable if necessary
    request.session.pop("bag_action", None)
    
    # Redirect to the referer URL or to a default fallback URL if not available
    redirect_url = request.META.get(
        "HTTP_REFERER", "default_fallback_url"
    )
    return HttpResponseRedirect(redirect_url)


@login_required
def toggle_wishlist(request, product_id):
    """Toggle the product's presence in the user's wishlist."""
    # Retrieve the product by ID, or return a 404 error if not found
    product = get_object_or_404(Product, id=product_id)
    # Get or create a WishlistItem for the product and the user
    wishlist_item, created = WishlistItem.objects.get_or_create(
        user=request.user, product=product
    )
    if created:
        # If the WishlistItem was newly created, add a success message
        request.session["wishlist_action"] = "added"
        message = f"{product.name} added to your wishlist."
    else:
        # If the WishlistItem already exists, delete it and add a success message
        wishlist_item.delete()
        request.session["wishlist_action"] = "removed"
        message = f"{product.name} removed from your wishlist."
    # Show the relevant success message
    messages.success(request, message)
    # Mark the session as modified
    request.session.modified = True

    # Redirect the user to the URL specified in the 'next' parameter or to a default view
    next_page = request.GET.get("next", reverse("view_wishlist"))
    return redirect(next_page)


@login_required
def view_wishlist(request):
    """Render the user's wishlist page."""
    # Retrieve all wishlist items for the logged-in user and order them by the date added
    wishlist_items = WishlistItem.objects.filter(user=request.user).order_by(
        "-added_on"
    )
    product_count = len(wishlist_items)
    message = None
    # Retrieve and remove any action message from the session
    if "wishlist_action" in request.session:
        action = request.session.pop("wishlist_action", None)
        message = f"Item {action} your wishlist."
        request.session.modified = True

    # Render the wishlist page with the items and message
    context = {
        "wishlist_items": wishlist_items,
        "product_count": product_count,
        "message": message,
    }
    return render(request, "wishlist/wishlist.html", context)


@login_required
def remove_from_wishlist(request, item_id):
    """Remove an item from the user's wishlist."""
    # Retrieve the WishlistItem by its ID, or return a 404 error if not found
    wishlist_item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
    # Delete the wishlist item
    wishlist_item.delete()
    # Add a success message indicating that the item was removed
    messages.success(
        request,
        "Item removed from your wishlist.",
    )
    # Redirect to the wishlist view
    return redirect("view_wishlist")


@login_required
def clear_wishlist_action(request):
    """Clear any wishlist-related action from the session."""
    if "wishlist_action" in request.session:
        del request.session["wishlist_action"]
    return HttpResponse("OK")
