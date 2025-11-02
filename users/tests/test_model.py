# users model tests
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            email='user@watchytest.com',
            password='letsTest?watchy'
        )
    
    def tearDown(self):
        del self.user

    def test_profile_creation(self):
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_default_values(self):
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.bio, 'No Bio added')
        self.assertEqual(profile.subscription_status, 'No Occupation added')
        self.assertEqual(profile.fav_actor, 'No favorite actor added')
        self.assertEqual(profile.fav_director, 'No favorite director added')
        self.assertEqual(profile.fav_genre, 'No favorite genre added')

    def test_blank_fields(self):
        profile = Profile.objects.get(user=self.user)
        self.assertIsNone(profile.date_of_birth)
