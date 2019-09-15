from django.test import TestCase
from django.test import Client
from django.urls import reverse

class StudentImportTestCase(TestCase):
    fixtures = ["test_datas.json"]

    def setUp(self):
        self.client = Client()
        self.url = reverse('students:student_import')
        self.client.login(username='sumee', password='sumee1910')

    def test_student_import_handsontable(self):
        
        handsontable_data = '[["Suhail","Vs","{}","04/12/1988"]]'

        # Blank Email
        response = self.client.post(self.url, {'classroom':1, 'data':handsontable_data.format('')})
        self.assertIn(b'All fields are required.', response.content)
        # 'All fields are required.'

        # Existing Email
        response = self.client.post(self.url, {'classroom':1, 'data':handsontable_data.format('suhail')})
        self.assertIn(b'Email:suhail already exists. Please provide different email.', response.content)
        # 'Email:<{}> already exists. Please provide different email.'.format(email)

        # Save Successfully
        response = self.client.post(self.url, {'classroom':1, 'data':handsontable_data.format('suhail@gmail.com')})
        self.assertIn(b'success', response.content)

    def test_check_student_tab_is_active(self):
        response = self.client.get(self.url)
        self.assertIn('<a class="nav-link active" href="{}">Students</a>'.format(reverse('students:user_list')).encode(), response.content)



class StudentMigrationTestCase(TestCase):
    fixtures = ["test_datas.json"]

    def setUp(self):
        self.client = Client()
        self.url = reverse('students:student_migration')
        self.client.login(username='sumee', password='sumee1910')
        # student = Student.objects.get(user=3)
        # Marks.objects.create(exam_id=2,subject_id=1,student=student,mark=20)
        # Marks.objects.create(exam_id=2,subject_id=2,student=student,mark=42)

    def test_studentmigration_forms(self):
        response = self.client.get(self.url)
        self.assertIn('<a class="nav-link active" href="{}">Student Migration</a>'.format(self.url).encode(), response.content)