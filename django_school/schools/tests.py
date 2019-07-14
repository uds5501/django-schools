from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from django.urls import reverse

class BaseTestCase(TestCase):
  fixtures = ["test_datas.json"]
  """Test who can add and view school"""
  def setUp(self):
    self.client = Client()
    
class UserPermissionTests(BaseTestCase):

  def test_url_for_permissions(self):
    # only teacher can change quiz
    for u in ['sumee','suhail']:
      self.client.login(username=u, password='sumee1910')
      response = self.client.get(reverse('teachers:quiz_change_list'))
      if u=='sumee': self.assertEqual(200,response.status_code)
      else: self.assertEqual(302,response.status_code)



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
        #last_name = selenium.find_element_by_id('id_last_name')

        submit = selenium.find_element_by_tag_name('button')

        #Fill the form with data
        
        username.send_keys('unary')
        selenium.implicitly_wait(10)
        #email.send_keys('yusuf@qawba.com')
        password1.send_keys('123456')
        password2.send_keys('123456')

        #submitting the form
        submit.send_keys(Keys.RETURN)
        # print(selenium.page_source)

        #check the returned result
        # assert 'This field is required.' in selenium.page_source