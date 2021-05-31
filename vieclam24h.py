from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import re
import csv





def  not_relative_uri(href):
	return re.compile('^https://').search(href) is  not  None
with open('/home/hiep/PycharmProjects/crawlJobData/linkvieclam24h.csv','rt')as f:
	data = csv.reader(f)
	for row in data:
		url = str(row)[2:-2]
		print(url)
		req = Request(url, headers={
			'User-Agent': 'Chrome/89.0.4389.128'
			})

		page = urlopen(req).read()

		soup = BeautifulSoup(page, 'html.parser')

		new_feeds = soup.find('div', class_='row job_detail').find_all('span', class_='job_value')



		data = []
		a= soup.find('h1',class_='title-job')
		b= soup.find('div', class_='title-company fs-16').find('a',class_='text-gray-75')
		c= soup.find('div', class_='col-12 col-md-6 list-info pt-0-mb').find('a', class_='job_value text-color-effect-second font500 underline text-join text-decoration hover-text-main')
		print(c.text)
		data.append(a.text)
		data.append(b.text)
		data.append(c.text)
		with open('vieclam24h.csv', 'a') as csv_file:
			writer = csv.writer(csv_file)

			for feed in new_feeds:
				 if'Hoa hồng' in str(feed.text):
					 continue
				 data.append(feed.text)
			writer.writerow(data)