from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category

class ProductViewsTests(TestCase):
    def setUp(self):
        """
        Set up a test client, and create a user and sample product.
        """
        self.client = Client()
        self.superuser = User.objects.create_superuser(username='superuser', password='superpassword')
        self.category = Category.objects.create(name='TestCategory')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            price=10.00
        )

    def test_all_products_view(self):
        """
        Test that the all_products view loads correctly.
        """
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view(self):
        """
        Test that the product detail view loads correctly.
        """
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)

    def test_add_product_view_superuser(self):
        """
        Test that a superuser can add a product.
        """
        self.client.login(username='superuser', password='superpassword')
        response = self.client.post(reverse('add_product'), {
            'name': 'New Product',
            'category': self.category.id,
            'price': '15.00',
            'description': 'A sample description',  
            'sku': 'NP123',                        
        })
        self.assertEqual(Product.objects.count(), 2)  

    def test_delete_product_view_superuser(self):
        """
        Test that a superuser can delete a product.
        """
        self.client.login(username='superuser', password='superpassword')
        response = self.client.post(reverse('delete_product', args=[self.product.id]))
        self.assertEqual(Product.objects.count(), 0)
