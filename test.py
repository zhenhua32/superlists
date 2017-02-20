from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
      # 打开首页
        self.browser.get('http://localhost:8000')

        # 首页有 'To-Do' 这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # 输入一个待办事项

        # 输入 'Buy an apple'

        # 按下回车, 页面更新
        # 页面上多了 '1: Buy an apple'

        # 页面上又显示了一个文本框, 可以再次输入待办事项
        # 再次输入 ' Buy a car'

        # 页面更新, 显示了两个待办事项

        # 网站生成了一个唯一的 URL
        # 页面中附带这个功能的说明

        # 访问这个 URL, 代办事项还在


if __name__ == '__main__':
    unittest.main(warnings='ignore')
