import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 打开首页
        self.browser.get('http://localhost:8000')
        time.sleep(3)

        # 首页有 'To-Do' 这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 输入 'Buy an apple'
        inputbox.send_keys('Buy an apple')

        # 按下回车, 页面更新
        # 页面上多了 '1: Buy an apple'
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy an apple', [row.text for row in rows])

        # 页面上又显示了一个文本框, 可以再次输入待办事项
        # 再次输入 ' Buy a car'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy a car')
        inputbox.send_keys(Keys.ENTER)

        # 页面更新, 显示了两个待办事项
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy an apple', [row.text for row in rows])
        self.assertIn('2: Buy a car', [row.text for row in rows])

        # 网站生成了一个唯一的 URL
        # 页面中附带这个功能的说明
        self.fail('Finish the test')
        # 访问这个 URL, 代办事项还在


if __name__ == '__main__':
    unittest.main(warnings='ignore')
