from django.test import TestCase
from django.test import Client

class QuizTestCase(TestCase):
    def setUp(self):
    	self.c = Client()

    def test_signup(self):
        response = self.c.post('/accounts/signup/student/',	{
        	"username": "admin",
            "password": 999,
        })
        self.assertIn('Usernames such as admin,students,teachers,quizzes,accounts are not allowed',response.content)
        self.assertEqual(response.status_code, 200)