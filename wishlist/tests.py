from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import WishlistItem
from products.models import Product


class WishlistViewsTests(TestCase):

    def setUp(self):
        """
        Set up the test client, test user, and sample product.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=10)

    def test_add_to_wishlist(self):
        """
        Test that a product can be added to the wishlist.
        """
        response = self.client.get(reverse('add_to_wishlist', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(WishlistItem.objects.filter(user=self.user, product=self.product).exists())

    def test_toggle_wishlist(self):
        """
        Test that the wishlist toggle adds or removes a product.
        """
        toggle_url = reverse('toggle_wishlist', args=[self.product.id])

        # Add the product to the wishlist
        response = self.client.get(toggle_url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(WishlistItem.objects.filter(user=self.user, product=self.product).exists())

        # Remove the product from the wishlist
        response = self.client.get(toggle_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(WishlistItem.objects.filter(user=self.user, product=self.product).exists())

    def test_view_wishlist(self):
        """
        Test that the wishlist page loads correctly.
        """
        WishlistItem.objects.create(user=self.user, product=self.product)
        response = self.client.get(reverse('view_wishlist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
