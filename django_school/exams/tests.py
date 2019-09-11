from django.test import TestCase
from django.test import Client
from django.urls import reverse

class ExamTestCase(TestCase):
    fixtures = ["test_datas.json"]

    def setUp(self):
        self.client = Client()
        self.url = reverse('exams:exams')
        self.client.login(username='sumee', password='sumee1910')

    def test_check_exams_tab_is_active(self):
        response = self.client.get(self.url)
        self.assertIn('<a class="nav-link active" href="{}">Exams</a>'.format(self.url).encode(), response.content)
