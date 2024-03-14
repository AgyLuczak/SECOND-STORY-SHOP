from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = Decimal('0')
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id in bag.keys():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price  
        product_count += 1  
        bag_items.append({
            'item_id': item_id,
            'quantity': 1,  
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / 100
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0')
        free_delivery_delta = Decimal('0')
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
