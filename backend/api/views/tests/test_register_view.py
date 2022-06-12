from test.common import TestingMixin
from core.models import User
from django.urls import reverse, resolve
from rest_framework.test import APIRequestFactory
from api.views import RegisterView

class Tests(TestingMixin):
    def test_url_mapping(self) -> None:
        self.assertEqual(resolve('/api/v1/auth/register/').func.__name__, RegisterView.__name__)

    def test_that_a_user_can_be_registered_through_the_api(self) -> None:
        """
        Executes a POST request to the API for the register endpoint, 
        and verifies that the user gets created properly.
        """
        self.assertEqual(User.objects.all().count(), 0)
        data = {
            "email": "testuser@yopmail.com",
            "password": "12345678",
            "username": "testuser"
        }
        request = APIRequestFactory().post("api/v1/auth/register/", data)
        

        view = RegisterView.as_view({"post": "create"})
        response = view(request, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.all().count(), 1)