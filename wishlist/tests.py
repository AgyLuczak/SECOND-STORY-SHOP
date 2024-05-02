from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product
from wishlist.models import WishlistItem

class WishlistViewsTests(TestCase):
    def setUp(self):
        """
        Set up the test client, create a test user, and create a sample product.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=10.00)
        self.client.login(username='testuser', password='testpassword')

    def test_add_to_wishlist(self):
        """
        Test adding a product to the wishlist.
        """
        response = self.client.get(reverse('add_to_wishlist', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(WishlistItem.objects.filter(user=self.user, product=self.product).exists())

    def test_view_wishlist(self):
        """
        Test viewing the wishlist.
        """
        WishlistItem.objects.create(user=self.user, product=self.product)
        response = self.client.get(reverse('view_wishlist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

    def test_remove_from_wishlist(self):
        """
        Test removing a product from the wishlist.
        """
        wishlist_item = WishlistItem.objects.create(user=self.user, product=self.product)
        response = self.client.post(reverse('remove_from_wishlist', args=[wishlist_item.id]))
        self.assertRedirects(response, reverse('view_wishlist'))
        self.assertFalse(WishlistItem.objects.filter(id=wishlist_item.id).exists())
