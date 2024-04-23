from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from products.models import Product

class MyTestCase(TestCase):
    def setUp(self):
        # Ensure the test database is used
        settings.DATABASES['default'] = dj_database_url.parse(os.getenv('TEST_DATABASE_URL'))
        super().setUp()


class BagViewsTestCase(TestCase):
    def setUp(self):
        # Create a sample product
        self.product = Product.objects.create(name="Test Product", price=Decimal('9.99'))
        self.client = Client()

    def test_add_to_bag(self):
        """ Test adding a product to the bag successfully """
        response = self.client.post(reverse('add_to_bag', args=[self.product.id]), 
                                    {'redirect_url': '/'})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)  # Expect redirect to success URL
        self.assertTrue(f'Added {self.product.name} to your bag.' in str(messages[0]))

    def test_add_to_bag_product_not_found(self):
        """ Test adding a non-existing product """
        response = self.client.post(reverse('add_to_bag', args=[999]), 
                                    {'redirect_url': '/'})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)  # Expect redirect to error URL
        self.assertTrue("Product not found." in str(messages[0]))

    def test_remove_from_bag(self):
        """ Test removing a product from the bag """
        self.client.session['bag'] = {str(self.product.id): 1}
        self.client.session.save()

        response = self.client.post(reverse('remove_from_bag', args=[self.product.id]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(f'Removed {self.product.name} from your bag.' in str(messages[0]))

    def test_remove_from_bag_product_not_found(self):
        """ Test removing a non-existing product from the bag """
        response = self.client.post(reverse('remove_from_bag', args=[999]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 404)
        self.assertTrue("Product not found." in str(messages[0]))
