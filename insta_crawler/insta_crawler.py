from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import os
import openpyxl
import urllib.request

filenameonly = 'list'

filename = filenameonly + '.xlsx'
book = openpyxl.load_workbook(filename)
sheet = book.worksheets[0]
input_list_1 = []
input_list_2 = []
for row in sheet.rows:
    input_list_1.append(row[0].value)

for row in sheet.rows:
    input_list_2.append(row[1].value)

print('GO!!')

driver = webdriver.Chrome('/HW/selenium/chromedriver')
time.sleep(2)
driver.implicitly_wait(3)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get(input_list_2[0])
driver.implicitly_wait(3)
time.sleep(2)

driver.get(input_list_2[0])
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button').click()
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('hwunderstand@gmail.com')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('k3246910!')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()


ro = 0

try:
    while ro < len(input_list_1):
        driver.get(input_list_2[ro])
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        img = soup.find_all('img')[1]

        img_src = img.get('src')


        urllib.request.urlretrieve(img_src, str(input_list_1[ro])+'.jpg')
        driver.implicitly_wait(3)
        ro=ro+1
        time.sleep(2)
except:
    driver.quit()



time.sleep(2)
driver.quit()
