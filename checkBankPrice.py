import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#货币选择
def countryCode(country_symbol):
    url = 'https://www.11meigui.com/tools/currency'
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    rows = soup.find_all('tr')
    data = []

    for row in rows:

        columns = row.find_all('td')

        for column in columns:
            row_str = column.get_text(strip=True) 
            data.append(row_str)

    index_num=data.index(country_symbol)
    return data[index_num-3]
#查询卖出价
def checkPrice(date):
    #爬虫
    driver = webdriver.Chrome()
    driver.get("https://www.boc.cn/sourcedb/whpj/")
    driver.maximize_window()
    sleep(2)

    #货币输入
    select=Select(driver.find_element(By.NAME,"pjname"))
    country_text=countryCode(country_symbol)
    select.select_by_visible_text(country_text)
    sleep(3)

    #日期输入
    driver.find_element(By.ID,"erectDate").click()
    driver.find_element(By.ID,"erectDate").clear()
    driver.find_element(By.ID,"erectDate").send_keys(date)
    sleep(3)

    #页面跳转
    #driver.find_element(By.ID,"historysearchform").click()
    el=driver.find_element(By.ID,"historysearchform")
    el.send_keys(Keys.ENTER)

    return date


#country_symbol,date=map(str,input().split(" "))
country_symbol=sys.argv[1]
date=sys.argv[2]
checkPrice(date)