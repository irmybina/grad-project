# This is a sample Python script.
import csv
from urllib.error import HTTPError
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
from selenium import webdriver
import phantomjs

import re
from scrapy import Item, Field

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     try:
#         html = urlopen("http://pythonscraping.com/pages/page1.html")
#         if html is None:
#             print("url not found")
#     except HTTPError as e:
#         print(e)
#     else:
#         bsObj = BeautifulSoup(html.read())
#     print(bsObj.h1)

# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html)
# # nameList = bsObj.findAll("span", {"class":"green"})
# nameList = bsObj.findAll(text="the prince")
# for name in nameList:
#     print(name.getText())

# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)
# for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# class Article(Item):
#     title = Field()
#
# class articleSpider(Spider):
#     name="article"
#     allowed_domains = ["en.wikipedia.org"]
#     start_urls = ["http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
#
# def parse(self, response):
#     item = Article()
#     title = response.xpath('//h1/text()')[0].extract()
#     print("Title is: " + title)
#     item['title'] = title
#     return item


# try:
#     html = urlopen("https://www.elibrary.ru/authors.asp")
#     if html is None:
#         print("url not found")
# except HTTPError as e:
#     print(e)
# else:
#     bsObj = BeautifulSoup(html.read())
# print(bsObj)

# session = requests.Session()
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
#
# url = "https://www.elibrary.ru/authors.asp"
# req = session.get(url, headers=headers)
#
# bsObj = BeautifulSoup(req.text)
# print(bsObj)

# params = {'username': 'Polina', 'password': 'password'}
# r = requests.post("https://pythonscraping.com/pages/cookies/wellcome.php", params)
# print("Cookie is set to: ")
# print(r.cookies.get_dict())
# print("Going to profile page...")
# r = requests.get("https://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
# print(r.text)

# session = requests.Session()
#
# s = session.post("https://pythonscraping.com/pages/cookies/wellcome.php", params)
# # print(s.cookies.get_dict())
# # s = session.get("https://pythonscraping.com/pages/cookies/profile.php")
# # print(s.text)
#
# auth = HTTPBasicAuth('polina', 'password')
#
# r = requests.post(url="https://pythonscraping.com/pages/cookies/login.html", auth=auth)
# print(r.text)

# session = requests.Session()
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
#            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#            "Accept-Language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#            "Viewport-Width":"958"}
#
# cookies = {"SCookieGUID":"66D3540D%2D2F58%2D4806%2DBA8B%2D7815173406F2",
#            "SUserID":"567933165",
#            "__utma":"216042306.342572815.1711982615.1711982615.1711982615.1",
#            "__utmb":"216042306.2.10.1711982615",
#            "__utmc":"216042306",
#            "__utmt":"1",
#            "__utmz":"216042306.1711982615.1.1.utmcsr=elibrary.ru|utmccn=(referral)|utmcmd=referral|utmcct=/",
#            "_ym_d":"1711982615",
#            "_ym_isad":"1",
#            "_ym_uid":"1685921343829450145",
#            "bh":"EkEiQ2hyb21pdW0iO3Y9IjEyMiIsICJOb3QoQTpCcmFuZCI7dj0iMjQiLCAiR29vZ2xlIENocm9tZSI7dj0iMTIyIhoFIng4NiIiECIxMjIuMC42MjYxLjEyOSIqAj8wOgkiV2luZG93cyJCCCIxNS4wLjAiSgQiNjQiUlwiQ2hyb21pdW0iO3Y9IjEyMi4wLjYyNjEuMTI5IiwiTm90KEE6QnJhbmQiO3Y9IjI0LjAuMC4wIiwiR29vZ2xlIENocm9tZSI7dj0iMTIyLjAuNjI2MS4xMjkiIg==",
#            }
#
# session.cookies.update(cookies)
#
# response = session.get("https://elibrary.ru/", headers=headers)
# print(response)


# session = requests.Session()
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
#            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#            "Accept-Language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#            "Viewport-Width":"958"}
#
# driver = webdriver.Chrome()
# driver.get("https://elibrary.ru/")
# driver.implicitly_wait(15)
#
# # cookies = driver.get_cookies()
# # session.cookies.update(driver.get_cookies())
#
# for cookie in driver.get_cookies():
#     session.cookies.set(cookie['name'], cookie['value'])
#
# response = session.get("https://elibrary.ru/", headers=headers)
# print(response)


# https://www.elibrary.ru/authors.asp?codetype=SPIN&rubriccode=&sortorder=0&orgadminid=&countryid=&town=&metrics=1&surname=&codevalue=&order=0&authors_all=&selid=&orgname=&pagenum=&authorbox_name=&orgid=


from selenium import webdriver

# Set up the WebDriver (make sure chromedriver is in your PATH or provide the path)
# driver = webdriver.Chrome()
#
# # Navigate to the URL
# # driver.get("https://www.elibrary.ru/authors.asp?codetype=SPIN&rubriccode=&sortorder=0&orgadminid=&countryid=&town=&metrics=1&surname=&codevalue=&order=0&authors_all=&selid=&orgname=&pagenum=&authorbox_name=&orgid=")
#
# # Get the HTML source of the page
# # html_source = driver.page_source
#
# # Save the HTML source to a file
# # with open("scrap.html", "w", encoding="utf-8") as file:
# #     file.write(html_source)
#
# # Close the browser
# driver.quit()
#
with open("scrap.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Now you can use BeautifulSoup methods to navigate and extract data from the HTML
# For example, to extract all links from the page:
table = soup.find("table", {'id':'restab'})

# Find all tr elements with bgcolor='#f5f5f5' within the table
rows = table.findAll('tr', {'bgcolor':'#f5f5f5'})

with open('output.csv', 'a', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)

    # Iterate over each tr element
    for row in rows:
        # Find all td elements within the current tr element
        cells = row.find_all('td')

        # for cell in cells:
        #     print("[")
        #     print(cell)
        #     print("]")
        #
        #
        # print("_____________________________________")

        a = (str)(cells[2]).split('<br/>')
        # print(a[0] + "AAAAAAAAA" + a[1])
        # print("____________")

        name = BeautifulSoup(a[0]).get_text()
        university = BeautifulSoup(a[1]).get_text()

        print(name + "AAAAAAAAA" + university)
        print("____________")

        publ = cells[3].get_text()
        cite = cells[4].get_text()
        hirsh = cells[5].get_text()

        # Extract text from the third td element (index 2) with special font properties
        # special_text = cells[2].split('<br>').get_text()

        # Extract text from the last three td elements
        # regular_text = ' / '.join(cell.get_text(strip=True) for cell in cells[-3:])

        # Combine the special and regular text with a separator
        # row_data = [special_text + ' / ' + regular_text]

        row_data = [name, university, publ, cite, hirsh]

        # Write the row data to the CSV file
        csvwriter.writerow(row_data)

print("Data saved to output.csv")


# print(soup.find("table", {'id':'restab'}).findAll('tr', {'bgcolor':'#f5f5f5'}))
