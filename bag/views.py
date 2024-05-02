from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product
from decimal import Decimal

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a specified product to the shopping bag."""
    try:
        # Retrieve the product based on the provided item_id
        product = Product.objects.get(pk=item_id)
        
        # Get the current bag from the session or initialize an empty dictionary
        bag = request.session.get('bag', {})

        # Check if the product is already in the bag
        if item_id in bag:
            messages.error(request, f'{product.name} is already in your bag.')
        else:
            # If not, add it to the bag with a quantity of 1
            bag[item_id] = 1 
            messages.success(request, f'Added {product.name} to your bag.')
           
        # Remove any wishlist-related session variables
        request.session.pop('wishlist_action', None)

        # Save the updated bag to the session
        request.session['bag'] = bag

    except Product.DoesNotExist:
        # Handle the case where the product does not exist
        messages.error(request, "Product not found.")
        
    # Redirect to the 'next' URL if provided, otherwise default to 'view_bag'
    next_page = request.GET.get('next', reverse('view_bag'))
    return redirect(next_page)


def remove_from_bag(request, item_id):
    """Remove the specified product from the shopping bag."""
    try:
        # Retrieve the product based on the provided item_id
        product = Product.objects.get(pk=item_id)

        # Get the current bag from the session or initialize an empty dictionary
        bag = request.session.get('bag', {})

        # Check if the product is in the bag
        if item_id in bag:
            # Remove the product from the bag
            del bag[item_id]
            messages.success(request, f'Removed {product.name} from your bag.')
        else:
            # If the product was not found in the bag, return an error message
            messages.error(request, f'{product.name} was not found in your bag.')

        # Save the updated bag to the session
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Product.DoesNotExist:
        # Handle the case where the product does not exist
        messages.error(request, "Product not found.")
        return HttpResponse(status=404)
    
    except Exception as e:
        # Handle any other exceptions and return a generic error message
        messages.error(request, "Error removing item from the bag.")
        return HttpResponse(status=500)
