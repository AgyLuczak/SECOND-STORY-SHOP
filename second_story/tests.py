from django.test import TestCase, Client, override_settings
from django.urls import path

# Sample view to raise server error
def test_500_view(request):
    raise Exception("This is a test exception to trigger 500.")

# Temporary URL pattern for testing 500 error
test_urlpatterns = [
    path('test-500/', test_500_view),
]

@override_settings(ROOT_URLCONF=__name__)
class ErrorPageTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_404_page(self):
        response = self.client.get('/non-existent-url/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_500_page(self):
        with self.settings(ROOT_URLCONF=__name__):
            response = self.client.get('/test-500/')
            self.assertEqual(response.status_code, 500)
            self.assertTemplateUsed(response, '500.html')
