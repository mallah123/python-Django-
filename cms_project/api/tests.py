from django.test import TestCase

# Create your tests here.
# api/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, ContentItem, Category
from .serializers import UserSerializer, ContentItemSerializer

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_registration(self):
        response = self.client.post('/api/register/', {'username': 'newuser', 'password': 'newpassword'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        response = self.client.post('/api/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

class ContentItemTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_content(self):
        response = self.client.post('/api/content/', {'title': 'Test Content', 'body': 'Lorem ipsum...', 'summary': 'Test summary'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContentItem.objects.count(), 1)

    def test_search_content(self):
        ContentItem.objects.create(title='Searchable Content', body='Searching...', summary='Search summary')
        response = self.client.get('/api/search/?search=Searchable')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
