from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import re
import csv


def not_relative_uri(href):
    return re.compile('^https://').search(href) is not None


with open('/home/hiep/PycharmProjects/crawlJobData/linkybox1.csv', 'rt')as f:
    data = csv.reader(f)
    for row in data:
        url = str(row)[2:-2]
        print(url)
        req = Request(url, headers={
            'User-Agent': 'Chrome/89.0.4389.128'
        })

        page = urlopen(req).read()

        soup = BeautifulSoup(page, 'html.parser')
        data = []
        title = soup.find("h3", class_='text-semibold mb-5 title').find('a').text
        end = title.find('Tuyển Dụng')
        company = title[:end]
        feeds = soup.find('div',
                          attrs={
                              "style": "background:#eaeaea;padding:15px;margin:10px 0 10px 0;border-radius:10px;"}).find_all(
            'span')
        begin = soup.text.find("@Tuyển dụng")
        end = soup.text.find("trước")
        time = soup.text[begin + 11:end + 5]

        for feed in feeds:
            feed = feed.text
            if feed.find("Kinh nghiệm:") > 0:
                kn = feed[14:]
            elif feed.find("Mức lương") > 0:
                salary = feed[11:]
            elif feed.find("Địa điểm") > 0:
                address = feed[10:]
            elif feed.find("Chuyên môn") > 0:
                chuyenmon = feed[12:]
            elif feed.find("Tính chất công việc") > 0:
                htlv = feed[21:]
        data.append(title)
        data.append(company)
        data.append(time)
        data.append(kn)
        data.append(salary)
        data.append(address)
        data.append(chuyenmon)
        data.append(htlv)

        with open('ybox.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(data)
