from django.test import TestCase, Client
from django.urls import reverse

class HomeViewsTest(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_index_page_loads_correctly(self):
        """
        Test that the index page loads correctly.
        """
        # Use the correct URL pattern name 'home'
        response = self.client.get(reverse('home'))
        
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template was used
        self.assertTemplateUsed(response, 'home/index.html')