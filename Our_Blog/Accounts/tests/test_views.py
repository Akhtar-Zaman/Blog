from django.test import TestCase, Client
from django.urls import reverse
from Accounts.models import Custom_User_Model
import json


class TestViews(TestCase):

    def setUp(self):
        self.CreateAccount_url = reverse('CreateAccount')
        self.Login_url = reverse('Login')
        self.signout_url = reverse('Login')



    def test_CreateAccount(self):
        response = self.client.get(self.CreateAccount_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_account.html')


    def test_Login(self):
        response = self.client.get(self.Login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'log.html')


    def test_signout(self):
        response = self.client.get(self.signout_url)

        self.assertEquals(response.status_code, 200)
        


        