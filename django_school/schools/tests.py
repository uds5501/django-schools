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
         password='secret',user_type = 4,is_staff=True,is_active=True)
    self.teacher = get_user_model().objects.create_user(username='some_user_teacher',
         password='secret',user_type = 2,is_staff=True,is_active=True)
    self.student = get_user_model().objects.create_user(username='some_user_student',
         password='secret',user_type = 1,is_staff=True,is_active=True) 
    
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
        self.assertIn('<strong>some_user_%s</strong>'%u
          ,response.content.decode())


from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumAccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()#Chrome('/home/suhailvs/Downloads')#webdriver.Firefox()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/accounts/signup/student/')
        #find the form element
        #first_name = selenium.find_element_by_id('id_first_name')
        #last_name = selenium.find_element_by_id('id_last_name')
        username = selenium.find_element_by_id('id_username')
        #email = selenium.find_element_by_id('id_email')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')

        school = selenium.find_element_by_id('id_school')
        #last_name = selenium.find_element_by_id('id_last_name')

        submit = selenium.find_element_by_tag_name('button')

        #Fill the form with data
        
        username.send_keys('unary')
        #email.send_keys('yusuf@qawba.com')
        password1.send_keys('123456')
        password2.send_keys('123456')
        school.send_keys('ASMMHSS')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        assert 'Check your email' in selenium.page_source