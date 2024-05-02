from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class TestProfilesViews(TestCase):

    def setUp(self):
        """
        Setup a test user and profile.
        """
        self.user = User.objects.create_user(
            username='testuser1',
            password='testpassword123'
        )
        self.profile_url = reverse('profile')

    def test_redirect_to_login_if_no_profile(self):
        """
        Test that accessing the profile URL redirects unauthenticated users to the login page.
        """
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_logged_in_user_can_access_profile(self):
        """
        Test that a logged-in user can access their profile.
        """
        self.client.login(username='testuser1', password='testpassword123')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
