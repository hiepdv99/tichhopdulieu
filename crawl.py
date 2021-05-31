from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import re
import csv

def  not_relative_uri(href):
	return re.compile('^https://').search(href) is  not  None
for i in range(1,6):
	url = 'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?q=&field_ids[]=146&action=search&page='+str(i)
	print(url)
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

	page = urlopen(req).read()


	soup = BeautifulSoup(page, 'html.parser')

	new_feeds = soup.find(
			'div', class_='box-list-job').findAll('a', class_='jsx-896248193')

	with open('linkvieclam24h.csv', 'a') as csv_file:
		writer = csv.writer(csv_file)
		j=1
		for feed in new_feeds:
			if not(j%2!=1):
				writer.writerow(['https://vieclam24h.vn'+feed.get('href')])
			j=j+1