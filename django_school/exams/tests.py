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

    def test_create_exam(self):
        # existing division
        params = {'name':'Class Test November','exam_class':10,'exam_date':'6/9/2019' }
        response = self.client.post(self.url, follow=True)
        self.assertIn(b'This field is required.', response.content)
        response = self.client.post(self.url,params, follow=True)
        self.assertIn(b'09 Jun 2019', response.content)

        # test get divisions of class for an exam
        # response = self.client.get(f"{reverse('exams:getdivisions')}?exam=15")
        # data = response.json()
        # self.assertEqual(data['is_grade'], False)
        # self.assertEqual(data['classes'], ['A'])

class MarkEntryTestCase(TestCase):
    fixtures = ["test_datas.json"]

    def setUp(self):
        self.client = Client()
        self.url = reverse('exams:markentry')
        self.client.login(username='sumee', password='sumee1910')
        # create an exam
        self.client.post(reverse('exams:exams'),{'name':'Class Test November','exam_class':10,'exam_date':'6/9/2019' })

    def test_check_markentry_tab_is_active(self):
        response = self.client.get(self.url)
        self.assertIn('<a class="nav-link active" href="{}">Mark Entry</a>'.format(self.url).encode(), response.content)

    def test_init_mark_entry_forms(self):
        response = self.client.get(self.url)
        self.assertIn(b'Class Test November (10)', response.content)

    