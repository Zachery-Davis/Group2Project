from django.test import TestCase
from django.contrib.auth import get_user_model
from application.form import RegisterForm, TreeForm
from django.contrib.auth.forms import AuthenticationForm

# Testing For Register Correctly
class RegisterUserTest(TestCase):
    def setUp(self):
       self.User = get_user_model()
    def test_register_form(self):
        form_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!",
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
    # When User Doesn't Fill The Form Correctly
    def test_missing_fields(self):
        form_data = {
            "email": "testuser@example.com",
            "password1": "StrongPassword123!",
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

# Testing For Logging In Correctly
class LoginUserTest(TestCase):
    def setUp(self):
        self.User = get_user_model()
        form_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!",
        }
        form = RegisterForm(data=form_data)
        if(form.is_valid()):
            user = form.save(commit=False)
            user.save()
    # Testing User Logging In Works Correctly
    def test_user_login(self):
        self.email = "testuser@example.com"
        self.password = "StrongPassword123!"
        logged_in = self.client.login(email=self.email, password=self.password)
        self.assertTrue(logged_in)
    # Testing If User Password Or Email Is Wrong
    def test_user_login_fail(self):
        self.email = "testuser@example.com"
        self.password = "idkThePassword"
        logged_in = self.client.login(email=self.email, password=self.password)
        self.assertFalse(logged_in)


        
    