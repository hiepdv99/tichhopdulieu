import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import csv

#Install Driver
driver = webdriver.Chrome(ChromeDriverManager().install())

#Specify Search URL
search_url= 'https://ybox.vn/tuyen-dung-viec-lam-lap-trinh-tk-c1d10?keyword='

driver.get(search_url.format(q='Car'))

#Scroll to the end of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(30)#sleep_between_interactions

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(30)#sleep_between_interactions

elems = driver.find_elements_by_xpath("//h2[contains(@class, 'post-title')]/a")
totalResults=len(elems)
print(totalResults)

with open('linkybox1.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for i in elems:
        print(i.get_attribute('href'))
        writer.writerow([i.get_attribute('href')])


driver.close()
