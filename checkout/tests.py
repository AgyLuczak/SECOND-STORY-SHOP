from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from checkout.models import Order
from products.models import Product
from decimal import Decimal

class CheckoutViewsTests(TestCase):
    def setUp(self):
        """
        Set up the test client, test user, and sample product.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=Decimal('10.00'))
        self.client.login(username='testuser', password='testpassword')
        self.bag_url = reverse('view_bag')
        self.checkout_url = reverse('checkout')
        self.checkout_success_url = reverse('checkout_success', args=['1234567890'])

    def test_checkout_view_get(self):
        """
        Test that the checkout view renders correctly with an empty bag.
        """
        response = self.client.get(self.checkout_url)
        self.assertRedirects(response, reverse('products'))

    def test_checkout_view_post(self):
        """
        Test that a valid checkout form submission creates an order and redirects.
        """
        # Add a product to the session bag
        session = self.client.session
        session['bag'] = {str(self.product.id): 1}
        session.save()

        # Make a POST request to the checkout view
        response = self.client.post(self.checkout_url, {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '123456789',
            'country': 'US',
            'postcode': '12345',
            'town_or_city': 'Test City',
            'street_address1': '123 Test Street',
            'street_address2': '',
            'county': 'Test County',
            'client_secret': 'test_client_secret_secret'
        })
        # Check that a new order was created and the user was redirected to the success page
        self.assertRedirects(response, reverse('checkout_success', args=[Order.objects.last().order_number]))

    def test_checkout_success_view(self):
        """
        Test that the checkout success view renders correctly.
        """
        # Create a test order
        order = Order.objects.create(
            order_number='1234567890',
            full_name='Test User',
            email='test@example.com',
            phone_number='123456789',
            country='US',
            postcode='12345',
            town_or_city='Test City',
            street_address1='123 Test Street',
            county='Test County',
        )
        response = self.client.get(reverse('checkout_success', args=[order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(response, order.order_number)
