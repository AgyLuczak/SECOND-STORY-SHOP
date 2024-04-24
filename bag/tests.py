from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from products.models import Product
from decimal import Decimal

class BagViewsTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", price=Decimal('9.99'))
        self.add_url = reverse('add_to_bag', args=[self.product.id])
        self.remove_url = reverse('remove_from_bag', args=[self.product.id])
        self.add_url_not_found = reverse('add_to_bag', args=[999])  # Non-existing product ID
        self.remove_url_not_found = reverse('remove_from_bag', args=[999])

    def test_add_to_bag_success(self):
        """Test successful addition of a product to the shopping bag."""
        response = self.client.post(self.add_url, {'redirect_url': '/'})
        messages = [str(message) for message in get_messages(response.wsgi_request)]
        self.assertEqual(response.status_code, 302)
        self.assertIn(f'Added {self.product.name} to your bag.', messages)

    def test_add_to_bag_product_not_found(self):
        """Test the addition of a non-existing product to the shopping bag."""
        response = self.client.post(self.add_url_not_found, {'redirect_url': '/'})
        messages = [str(message) for message in get_messages(response.wsgi_request)]
        self.assertEqual(response.status_code, 302)
        self.assertIn("Product not found.", messages)

    def test_remove_from_bag_success(self):
        """Test successful removal of a product from the bag."""
        # Simulate adding product to bag first
        self.client.session['bag'] = {str(self.product.id): 1}
        self.client.session.save()

        response = self.client.post(self.remove_url)
        messages = [str(message) for message in get_messages(response.wsgi_request)]
        self.assertEqual(response.status_code, 200)
        self.assertIn(f'Removed {self.product.name} from your bag.', messages)

    def test_remove_from_bag_product_not_found(self):
        """Test the removal of a non-existing product from the shopping bag."""
        response = self.client.post(self.remove_url_not_found)
        messages = [str(message) for message in get_messages(response.wsgi_request)]
        self.assertEqual(response.status_code, 404)
        self.assertIn("Product not found.", messages)
