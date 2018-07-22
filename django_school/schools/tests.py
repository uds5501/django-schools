from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from django.urls import reverse

class BaseTestCase(TestCase):
  """Test who can add and view school"""
  def setUp(self):
    self.client = Client()
    self.admin = get_user_model().objects.create_user(username='some_user_admin',
         password='secret',user_type = 5,is_superuser=True,is_staff=True,is_active=True)
    # create principal
    self.principal = get_user_model().objects.create_user(username='some_user_principal',
         password='secret',user_type = 4)
    self.teacher = get_user_model().objects.create_user(username='some_user_teacher',
         password='secret',user_type = 2)
    self.student = get_user_model().objects.create_user(username='some_user_student',
         password='secret',user_type = 1) 
    
class UserPermissionTests(BaseTestCase):

  def test_url_for_permissions(self):
    # only teacher can change quiz
    for u in ['admin','principal','teacher','student']:
      self.client.login(username='some_user_'+u, password='secret')
      response = self.client.get(reverse('teachers:quiz_change_list'))
      if u=='teacher': self.assertEqual(200,response.status_code)
      else: self.assertEqual(302,response.status_code)


class HomePageTests(BaseTestCase):

  def test_homepage_urls(self):
    # teacher homepage, student homepage, admin homepage
    for u in ['guest','admin','principal','teacher','student']:
      self.client.login(username='some_user_'+u, password='secret')
      response = self.client.get('/')
      if u == 'guest':
        # if guest redirect to login page?
        self.assertEqual(302,response.status_code)
        # self.assertIn('<h2>Log in</h2>',response.content.decode())
      else:
        self.assertEqual(200,response.status_code)
        self.assertIn('Logged in as <strong>some_user_%s</strong>'%u
          ,response.content.decode())
       