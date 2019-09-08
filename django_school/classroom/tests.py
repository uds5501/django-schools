from django.test import TestCase, Client

from django.urls import reverse

class LoginPageTest(TestCase):
	fixtures = ["test_datas.json"]

	def setUp(self):
		self.client = Client()

	def test_login_page_returns_correct_html(self):
		loginurl = reverse('login')
		response = self.client.get(loginurl)
		self.assertEqual(response.status_code,200)
		# test response contains Username and Password
		self.assertIn(b'Username', response.content)
		self.assertIn(b'Password', response.content)

		# blank fields
		response = self.client.post(loginurl)
		self.assertIn(b'This field is required.', response.content)
		
		# wrong username or password
		response = self.client.post(loginurl, {'username':'bad', 'password':'bad'})
		self.assertIn(b'Please enter a correct username and password.', response.content)

	def test_login_as_teacher(self):
		loginurl = reverse('login')
		# login as teacher
		response = self.client.post(loginurl, {'username':'sumee', 'password':'sumee1910'}, follow=True)
		# print(response.content)
		# self.assertEqual(response.redirect_chain[1][0],reverse('teachers:quiz_change_list'))
		self.assertIn(b'G. H. S. S. Kizhakkanchery', response.content)


class UserPermissionsTest(TestCase):
	fixtures = ["test_datas.json"]

	def setUp(self):
		self.client = Client()

	def test_anonymous_user_will_not_visit_teacher_pages(self):
		response = self.client.get(reverse('classroom:timetable'), follow=True)
		self.assertIn(b'<button type="submit" class="btn btn-primary">Log in</button>', response.content)

	def test_teacher_can_visit_timetable(self):
		self.client.login(username='sumee', password='sumee1910')
		response = self.client.get(reverse('classroom:timetable'))
		self.assertIn(b'<a class="nav-link active" href="/classroom/timetable/">Timetable</a>', response.content)


class TimeTablePageTest(TestCase):
	fixtures = ["test_datas.json"]

	def setUp(self):
		self.client = Client()

	def test_teacher_timetable(self):
		self.client.login(username='sumee', password='sumee1910')
		response = self.client.get(reverse('classroom:timetable'))
		# print(response.content)



class AttendanceTest(TestCase):
	fixtures = ["test_datas.json"]

	def setUp(self):
		self.client = Client()

	def test_only_verified_user_show_in_attendance(self):
		self.client.login(username='sumee', password='sumee1910')
		response = self.client.get(reverse('classroom:attendance'),{'classroom':1,'date':'04/09/2019'})
		self.assertNotIn(b'<td>sufail</td>', response.content)
