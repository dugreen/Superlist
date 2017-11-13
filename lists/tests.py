from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

from django.http import HttpRequest
from django.template.loader import render_to_string

# 测试确认可以运行测试代码
# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1+1,5)


class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))#AssertionError 认定错误
        self.assertIn(b'<title>To-Do lists</title>',response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),expected_html)

        
