from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

# 打开首页
browser.get('http://localhost:8000')

# 首页有 'Django' 这个词
assert 'Django' in browser.title

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

browser.quit()
