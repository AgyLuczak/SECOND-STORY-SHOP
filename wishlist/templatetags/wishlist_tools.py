from django import template
from wishlist.models import WishlistItem

register = template.Library()


@register.filter(name="is_in_wishlist")
def is_in_wishlist(product, user):
    return WishlistItem.objects.filter(user=user, product=product).exists()
