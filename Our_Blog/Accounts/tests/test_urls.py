from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Accounts.views import CreateAccount, activate, Login, signout, change_password, profile



class TestUrls(SimpleTestCase):

    def test_CreateAccount_url(self):
        url = reverse('CreateAccount')
        self.assertEquals(resolve(url).func, CreateAccount)


    def test_Login_url(self):
        url = reverse('Login')
        self.assertEquals(resolve(url).func, Login)



    def test_signout_url(self):
        url = reverse('signout')
        self.assertEquals(resolve(url).func, signout)


    def test_change_password(self):
        url = reverse('change_password')
        self.assertEquals(resolve(url).func, change_password)


    def test_profile_url(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)



    def test_activate_url(self):
         url = reverse('activate', args=['uidb64','token'] )
         self.assertEquals(resolve(url).func, activate)
