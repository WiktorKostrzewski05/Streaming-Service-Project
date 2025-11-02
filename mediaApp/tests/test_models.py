# mediaApp Model Test
from django.test import TestCase
from mediaApp.models import Genre, Content
import datetime

class ContentModelTestCase(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(type_genre='Crime')
        self.content = Content.objects.create(
            con_title='Test Content Title',
            con_description='This is testing the content description.',
            con_released=datetime.datetime(2024, 2, 16),
            con_upload_date=datetime.datetime(2024, 2, 17),
            con_withdrawal_date=None,
            con_available=True
        )
        self.content.con_genre.add(self.genre)

    def test_content_title(self):
        self.assertEqual(self.content.con_title, 'Test Content Title')

    def test_content_description(self):
        self.assertEqual(self.content.con_description, 'This is testing the content description.')
    
    def test_content_released(self):
        self.assertEqual(self.content.con_released, datetime.datetime(2024, 2, 16))

    def test_content_upload_date(self):
        self.assertEqual(self.content.con_upload_date, datetime.datetime(2024, 2, 17))

    def test_content_withdrawal_date(self):
        self.assertEqual(self.content.con_withdrawal_date, None)

    def test_content_available(self):
        self.assertEqual(self.content.con_available, True)
    
    def tearDown(self):
        del self.genre
        del self.content
