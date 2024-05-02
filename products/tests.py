from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product, Category

class ProductViewsTests(TestCase):

    def setUp(self):
        """
        Set up a test user and sample product data.
        """
        # Create a test user with superuser privileges
        self.user = User.objects.create_superuser(username='admin', password='password')
        self.client.login(username='admin', password='password')

        # Create sample category and product data
        self.category = Category.objects.create(name='Category1', friendly_name='Category 1')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            price=10.00
        )

    def test_all_products_view(self):
        """
        Test that the all products view loads correctly.
        """
        response = self.client.get(reverse('products:all_products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_delete_product_view_superuser(self):
        """
        Test that a superuser can delete a product.
        """
        response = self.client.post(reverse('products:delete_product', args=[self.product.id]))
        self.assertRedirects(response, reverse('products:all_products'))
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())
