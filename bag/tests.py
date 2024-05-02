from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from products.models import Product

class BagViewsTests(TestCase):
    def setUp(self):
        """
        Set up the test client, test user, and sample product.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=Decimal('10.00'))

    def test_view_bag(self):
        """
        Test that the bag view renders correctly.
        """
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        """
        Test that a product can be added to the shopping bag.
        """
        response = self.client.post(reverse('add_to_bag', args=[self.product.id]))
        self.assertRedirects(response, reverse('view_bag'))
        bag = self.client.session.get('bag', {})
        self.assertIn(str(self.product.id), bag)

    def test_add_existing_to_bag(self):
        """
        Test that adding an already existing product to the bag gives an error.
        """
        # Add product to the bag
        self.client.post(reverse('add_to_bag', args=[self.product.id]))
        
        # Try to add the product again
        response = self.client.post(reverse('add_to_bag', args=[self.product.id]))
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertTrue(any(str(message) == f'{self.product.name} is already in your bag.' for message in messages_list))

    def test_remove_from_bag(self):
        """
        Test that a product can be removed from the shopping bag.
        """
        # Add product to the bag first
        self.client.post(reverse('add_to_bag', args=[self.product.id]))

        # Now remove it
        response = self.client.post(reverse('remove_from_bag', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        bag = self.client.session.get('bag', {})
        self.assertNotIn(str(self.product.id), bag)
