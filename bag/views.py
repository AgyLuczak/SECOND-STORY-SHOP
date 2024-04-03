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
        product = Product.objects.get(pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            messages.error(request, f'{product.name} is already in your bag.')
        else:
            bag[item_id] = 1  # Indicate the product is present in the bag
            messages.success(request, f'Added {product.name} to your bag.')

        request.session['bag'] = bag
        # Provide a default URL name as a fallback for the redirect
        return redirect(request.POST.get('redirect_url', 'view_bag'))
    except Product.DoesNotExist:
        messages.error(request, "Product not found.")
        return redirect('view_bag')
        

def remove_from_bag(request, item_id):
    """Remove the specified product from the shopping bag."""
    try:
        product = Product.objects.get(pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            del bag[item_id]
            messages.success(request, f'Removed {product.name} from your bag.')
        else:
            messages.error(request, f'{product.name} was not found in your bag.')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Product.DoesNotExist:
        messages.error(request, "Product not found.")
        return HttpResponse(status=404)
    except Exception as e:
        messages.error(request, "Error removing item from the bag.")
        return HttpResponse(status=500)