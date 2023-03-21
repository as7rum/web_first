from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from blog.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_hime_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        requests = HttpRequest
        response = home_page(requests)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Сайт Айнара Ерошенкова</title>', html)
        self.assertIn('<h1>Айнар Ерошенков</h1>', html)
        self.assertTrue(html.endswith('</html>'))
