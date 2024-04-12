from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    bag_items = []
    product_count = 0  # Initialize product count to zero
    total = Decimal('0')
    running_total = Decimal('0')  
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        product_count += quantity  # Increment product count directly based on quantity
        price = product.price * quantity
        running_total += price  # Update running total with each item
        bag_items.append({
            'item_id': item_id,
            'product': product,
            'quantity': quantity,
            'price': price,
            'subtotal': running_total,  # Use the running total as the cumulative subtotal for each item
        })

    delivery = Decimal('0')
    free_delivery_delta = Decimal('0')
    if running_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = running_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / 100
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - running_total

    grand_total = delivery + running_total

    context = {
        'bag_items': bag_items,
        'product_count': product_count,  
        'total': running_total,  
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context


# Social links
def social_links(request):
    return {
        'social_links': settings.SOCIAL_LINKS
    }