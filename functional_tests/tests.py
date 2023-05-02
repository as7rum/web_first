from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from blog.models import Article
from datetime import datetime
import pytz

class BasicInstallTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='ooo-lya-lya',
        )

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):

        #в браузере П. открывает сайт по адресу http://127.0.0.1:8000
        # В заголовке сайта указано "Сайт Айнара Ерошенкова"
        self.browser.get(self.live_server_url)
        self.assertIn('Сайт Айнара Ерошенкова', self.browser.title)
        # self.fail('Finish the test!')

    def test_home_page_title(self):

        #в браузере П. открывает сайт по адресу http://127.0.0.1:8000
        # В заголовке сайта указано "Сайт Айнара Ерошенкова"
        self.browser.get(self.live_server_url)
        header = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Айнар Ерошенков', header)
        # self.fail('Finish the test!')

    def test_home_page_blog(self):
        #под шапкой расположен блог со статьями
        self.browser.get(self.live_server_url)
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        # У каждой статьи есть заголовок и один абзац с текстом
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_summary = self.browser.find_element(By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

    def test_home_page_article_title_link_leads_to_article_page(self):
        # Переход на новую страницу статьи с ее полным текстом

        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_title_text = article_title.text
        
        # находим ссылку в заголовке статьи
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        self.browser.get(article_link.get_attribute('href'))
        article_page_title = self.browser.find_element(By.CLASS_NAME, 'article-title')

        self.assertEqual(article_title_text, article_page_title.text)

