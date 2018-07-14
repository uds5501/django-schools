from django.test import TestCase
from .models import Quiz,Question, Answer
from django.test import Client

class QuizTestCase(TestCase):
    def setUp(self):
    	self.c = Client()

    def test_quiztest_url(self):
        response = self.c.get('/quizzes/')
        print (response.content)
        print (response.status_code)
        self.assertEqual(response.status_code, 401)