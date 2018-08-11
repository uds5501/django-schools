from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

class TeacherTestCase(TestCase):
    """Teacher pages tests"""
    def setUp(self):
        self.client = Client()
        self.teacher = get_user_model().objects.create_user(username='some_user_teacher',
         password='secret',user_type = 2)

    def test_homepage_urls(self):
        self.client.login(username='some_user_teacher', password='secret')
        for u in ['quiz_change_list','student_list',]: #'teachers','attendence','events','dashboard',]:            
            response = self.client.get(reverse('teachers:%s'%u))            
            self.assertEqual(200,response.status_code)

class UrlsTest(TestCase):

    def test_responses(self, allowed_http_codes=[200, 302, 405],
            credentials={}, logout_url="", default_kwargs={}, quiet=True):
        """
        Test all pattern in root urlconf and included ones.
        Do GET requests only.
        A pattern is skipped if any of the conditions applies:
            - pattern has no name in urlconf
            - pattern expects any positinal parameters
            - pattern expects keyword parameters that are not specified in @default_kwargs
        If response code is not in @allowed_http_codes, fail the test.
        if @credentials dict is specified (e.g. username and password),
            login before run tests.
        If @logout_url is specified, then check if we accidentally logged out
            the client while testing, and login again
        Specify @default_kwargs to be used for patterns that expect keyword parameters,
            e.g. if you specify default_kwargs={'username': 'testuser'}, then
            for pattern url(r'^accounts/(?P<username>[\.\w-]+)/$' 
            the url /accounts/testuser/ will be tested.
        If @quiet=False, print all the urls checked. If status code of the response is not 200,
            print the status code.
        """
        import importlib
        module = importlib.import_module(settings.ROOT_URLCONF)
        if credentials:
            self.client.login(**credentials)
        def check_urls(urlpatterns, prefix=''):
            for pattern in urlpatterns:
                if hasattr(pattern, 'url_patterns'):
                    # this is an included urlconf
                    new_prefix = prefix
                    if pattern.namespace:
                        new_prefix = prefix + (":" if prefix else "") + pattern.namespace
                    check_urls(pattern.url_patterns, prefix=new_prefix)
                params = {}
                skip = False
                regex = pattern.pattern.regex
                if regex.groups > 0:
                    # the url expects parameters
                    # use default_kwargs supplied
                    if regex.groups > len(regex.groupindex.keys()) \
                        or set(regex.groupindex.keys()) - set(default_kwargs.keys()):
                        # there are positional parameters OR
                        # keyword parameters that are not supplied in default_kwargs
                        # so we skip the url
                        skip = True
                    else:
                        for key in set(default_kwargs.keys()) & set(regex.groupindex.keys()):
                            params[key] = default_kwargs[key]
                if hasattr(pattern, "name") and pattern.name:
                    name = pattern.name
                else:
                    # if pattern has no name, skip it
                    skip = True
                    name = ""
                fullname = (prefix + ":" + name) if prefix else name
                if not skip:
                    url = reverse(fullname, kwargs=params)
                    response = self.client.get(url)
                    self.assertIn(response.status_code, allowed_http_codes)
                    # print status code if it is not 200
                    status = "" if response.status_code == 200 else str(response.status_code) + " "
                    if not quiet:
                        print(status + url)
                    if url == logout_url and credentials:
                        # if we just tested logout, then login again
                        self.client.login(**credentials)
                else:
                    if not quiet:
                        print("SKIP " + regex.pattern + " " + fullname)
        check_urls(module.urlpatterns)

