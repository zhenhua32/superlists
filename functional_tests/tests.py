import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


class NewVistorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 第一个用户打开首页
        self.browser.get(self.live_server_url)
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

        # 按下回车, 被带到了一个新URL
        # 这个页面的待办事项清单中显示了"1: Buy an apple"
        inputbox.send_keys(Keys.ENTER)
        first_list_url = self.browser.current_url
        self.assertRegex(first_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy an apple')

        # 页面上又显示了一个文本框, 可以再次输入待办事项
        # 再次输入 ' Buy a car'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy a car')
        inputbox.send_keys(Keys.ENTER)

        # 页面更新, 显示了两个待办事项
        self.check_for_row_in_list_table('1: Buy an apple')
        self.check_for_row_in_list_table('2: Buy a car')

        # 现在一个新用户访问了网站

        # #使用一个新浏览器会话
        # #确保第一个用户的信息不会从cookie中泄漏出来
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # 第二个用户访问首页
        # 页面中看不到第一个用户的清单
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy an apple', page_text)
        self.assertNotIn('Buy a car', page_text)

        # 第二个用户输入一个新待办事项, 新建一个清单
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # 获得唯一URL
        second_list_url = self.browser.current_url
        self.assertRegex(second_list_url, '/lists/.+')
        self.assertNotEqual(second_list_url, first_list_url)

        # 这个页面中没有第一个用户的清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy an apple', page_text)
        self.assertNotIn('Buy a car', page_text)

        # 页面中附带这个功能的说明
        self.fail('Finish the test')
        # 访问这个 URL, 代办事项还在


if __name__ == '__main__':
    unittest.main(warnings='ignore')
