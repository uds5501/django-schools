from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .models import Marks, Exam
from students.models import Student

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


class MarkEntryTestCase(TestCase):
    fixtures = ["test_datas.json"]

    def setUp(self):
        self.client = Client()
        self.url = reverse('exams:markentry')
        self.client.login(username='sumee', password='sumee1910')
        # create an exam
        # self.client.post(reverse('exams:exams'),{'name':'Class Test November','exam_class':10,'exam_date':'6/9/2019' })

    def test_check_markentry_tab_is_active(self):
        response = self.client.get(self.url)
        self.assertIn('<a class="nav-link active" href="{}">Mark Entry</a>'.format(self.url).encode(), response.content)

    def test_init_mark_entry_forms(self):
        response = self.client.get(self.url)
        self.assertIn(b'Class Test November (10)', response.content)

    def test_get_classrooms_ajax(self):
        # test get classrooms for an exam
        response = self.client.get(reverse('exams:getajaxdata'), {'exam':1})
        data = response.json()
        self.assertEqual(data['is_grade'], True)
        self.assertEqual(data['classes'], [{'classroom':'10A','id':1}])

        # handsontable load student data 
        response = self.client.get(reverse('exams:getajaxdata'), {'exam':1, 'classroom':1,'subject':1})
        data = response.json()
        self.assertIn([3, 'Suhail VS', ''],data['students'])
        # inactive student not in list
        self.assertNotIn([4, 'Sufail VS', ''],data['students'])

    def test_save_markentry(self):
        handsontable_data = '[["3","Suhail VS","{}"]]'
        # Blank Grade
        response = self.client.post(self.url, {'exam':1,'subject':1, 'data':handsontable_data.format('')})
        self.assertEqual(Marks.objects.filter(exam=1,subject=1,student__user=3).count(), 0)

        # Valid Grade
        response = self.client.post(self.url, {'exam':1,'subject':1, 'data':handsontable_data.format('a+')})
        markentry = Marks.objects.filter(exam=1,subject=1,student__user=3)
        self.assertEqual(markentry.count(), 1)
        self.assertEqual(markentry[0].grade, 'A+')

        # Edit Grade
        response = self.client.post(self.url, {'exam':1,'subject':1, 'data':handsontable_data.format('c+')})
        markentry = Marks.objects.filter(exam=1,subject=1,student__user=3)
        self.assertEqual(markentry.count(), 1)
        self.assertEqual(markentry[0].grade, 'C+')
    
        # Mark
        params = {'exam':2,'subject':1,'data':handsontable_data.format('')}
        # Blank Mark
        response = self.client.post(self.url, params)
        self.assertIn(b'Max Mark and Pass Mark is required.', response.content)

        params['max_mark'] = 50
        params['pass_mark'] = 20
        params['data'] = handsontable_data.format('20')
        # Valid Mark
        response = self.client.post(self.url, params)
        self.assertIn(b'success', response.content)
        markentry = Marks.objects.filter(exam=params['exam'],subject=params['subject'],student__user=3)
        self.assertEqual(markentry.count(), 1)
        self.assertEqual(markentry[0].mark, 20)

        # Mark greater than Max Marks
        params['data'] = handsontable_data.format('100')
        response = self.client.post(self.url,params)
        self.assertIn(b'Error: Student mark is greater than Maximum Mark.', response.content)

        # Prevent entering Grade for an Exam with Marks
        params['data'] = handsontable_data.format('c+')
        response = self.client.post(self.url,params)
        self.assertIn(b'Please provide mark as Interger.', response.content)

class ExamReportTestCase(TestCase):
    fixtures = ["test_datas.json"]

    def setUp(self):
        self.client = Client()
        self.url = reverse('exams:examreports')
        self.client.login(username='sumee', password='sumee1910')
        student = Student.objects.get(user=3)
        Marks.objects.create(exam_id=2,subject_id=1,student=student,mark=20)
        Marks.objects.create(exam_id=2,subject_id=2,student=student,mark=42)

    def test_examreport_forms(self):
        response = self.client.get(self.url)
        self.assertIn('<a class="nav-link active" href="{}">Exam Reports</a>'.format(self.url).encode(), response.content)
        # Exam Select box has option 'Class Test November (10)'
        # self.assertIn(b'Class Test November (10)', response.content)

    def test_examreport_of_class(self):
        response = self.client.get(self.url,{'classroom':1,'exam':2})
        self.assertIn(b'<td>Suhail VS</td>', response.content)
        self.assertIn(b'<td>62</td>', response.content)

    def test_examreport_of_class_old_academicyear(self):
        """
        Exam report of an old academicyear of a passout student

        """
        exam = Exam.objects.create(school_id = 1, academicyear_id =1, name='Old Exam', exam_class=10, exam_date="2019-06-09")
        Marks.objects.create(exam=exam, subject_id=1, student=Student.objects.get(user=5), mark=20)
        response = self.client.get(self.url,{'classroom':1,'exam':exam.id})
        self.assertIn(b'<td>Saji S</td>', response.content)

    def test_barchart_of_student(self):
        # {% url 'exams:barchart' exam=v1 student=v2 %}
        url = reverse('exams:barchart', kwargs={'exam':2,'student':3})
        response = self.client.get(url)
        
        self.assertIn(b'Social Class November Test Marks', response.content)

