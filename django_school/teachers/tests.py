from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

class TeacherTestCase(TestCase):
    fixtures = ["test_datas.json"]
    """Teacher pages tests"""
    def setUp(self):
        self.client = Client()

    def test_homepage_urls(self):
        self.client.login(username='sumee', password='sumee1910')
        for u in ['quiz_change_list','events']: #'teachers','attendence','events','dashboard',]:            
            response = self.client.get(reverse(f'teachers:{u}'))            
            self.assertEqual(200,response.status_code)

        for usertype in [1,2]:
            # teacher list & student list
            self.client.get(reverse(f'teachers:user_list', args=(usertype,)))
            self.assertEqual(200,response.status_code)