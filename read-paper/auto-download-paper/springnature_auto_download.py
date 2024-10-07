import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

from springer import basic_url

# 你的网址列表
urls = [
    'https://www.nature.com/articles/s41558-024-02137-5.pdf',
    'https://www.nature.com/articles/s41558-024-01950-2.pdf',

    # 更多网址...
]
basic_url = 'https://www.nature.com/articles/s41558-024-02137-5.pdf'
# 设置Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(basic_url)


for url in urls:
    driver.get(url)


    # 等待页面加载完成
    driver.implicitly_wait(10)
    sleep_time = random.randint(0, 20)
    time.sleep(sleep_time)
# 关闭浏览器
driver.quit()
