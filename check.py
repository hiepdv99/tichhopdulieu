import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import csv
from selenium import webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())

loginurl = 'https://www.topcv.vn/login'
driver.get(loginurl)

login = driver.find_element_by_xpath("//input[@type='email']").send_keys('dongvanhiep92@gmail.com')
password = driver.find_element_by_xpath("//input[@type='password']").send_keys('123456')
submit = driver.find_element_by_xpath("//input[@value='Đăng Nhập']").click()

url = 'https://www.topcv.vn/viec-lam/junior-android-developer/390971.html?ta_source=JobSearchList'
print(url)

driver.get(url)
time.sleep(3)


elems = driver.find_elements_by_xpath("//div[contains(@class, 'job-info-item')]/span")
totalResults = len(elems)

title = driver.find_elements_by_xpath("//h1[contains(@class = 'job-title text-highlight bold text-uppercase', @style = 'overflow-wrap:break-word;')]/a")
company = driver.find_elements_by_xpath("//div[(@class = 'company-title')]/span")[0].text
x = driver.find_elements_by_xpath("//div[contains(@class, 'job-deadline')]")
df = []
for ti in title:
						df.append(ti.text)
df.append(company)
for tim in x:
					df.append(tim.get_attribute("innerHTML")[-11:-1])




with open('topcv.csv', 'a') as csv_file:
							writer = csv.writer(csv_file)
							j = 1

							for i in elems:
								if j == 1:
									df.append(i.get_attribute("innerHTML")[1:-1])
								elif j == 7:
									index = i.get_attribute("innerHTML").find('>')
									end = i.get_attribute("innerHTML").find('</a>')
									df.append(i.get_attribute("innerHTML")[index + 1:end])
								else:
									df.append(i.get_attribute("innerHTML"))
								j = j + 1

							writer.writerow(df)
driver.close()