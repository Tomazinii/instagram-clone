from django.test import TestCase
# from .models import CustomUser
# Create your tests here.


class UserTest(TestCase):
    def test_verify_custom_user_class(self):
        user = CustomUser.objects.filter(id=1)
        self.assertEqual(user, True)