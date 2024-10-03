from django.test import TestCase
from django.contrib.auth.models import User

class TestModels(TestCase):
    def setUp(self) -> None:
        super().setUp()
        User.objects.create(username="sreedhar742",email='psreedhar742@gmail.com',first_name="sreedhar",last_name="pp",password1="car@123@CAR",password2="car@123@CAR",)