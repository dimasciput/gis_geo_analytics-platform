"""Test create instance."""
from django.contrib.auth import get_user_model
from django.test import Client
from django.test.testcases import TestCase
from django.urls import reverse

from gap_data.models.instance import Instance
from gap_data.tests.model_factories import UserF

User = get_user_model()


class InstanceCreateTest(TestCase):
    """Test create instance."""

    def setUp(self):
        """To setup test."""
        self.url = reverse(
            'instance-management-create'
        )
        self.data = {
            'name': 'Instance 1'
        }

    def test_save_level_no_login(self):
        """Test save level no login."""
        client = Client()
        response = client.post(self.url, data=self.data)
        self.assertEquals(response.status_code, 302)

    def test_save_level_not_staff(self):
        """Test save level non staff."""
        username = 'test'
        password = 'testpassword'
        UserF(username=username, password=password, is_superuser=False)
        client = Client()
        client.login(username=username, password=password)
        response = client.post(self.url, data=self.data)
        self.assertEquals(response.status_code, 302)

    def test_save_level_staff(self):
        """Test save level staff."""
        username = 'admin'
        password = 'adminpassword'
        UserF(username=username, password=password, is_superuser=True)
        client = Client()
        client.login(username=username, password=password)
        response = client.post(self.url, data=self.data)
        self.assertEquals(response.status_code, 302)
        self.assertTrue(
            Instance.objects.filter(name=self.data['name']).first()
        )
