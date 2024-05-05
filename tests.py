import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}


# Example URL to scrape
url = 'https://2ip.ru/'

# Example list of proxies
proxies = {
    # 'http': 'http://username:password@proxy_ip:proxy_port',
    'https': '18.223.25.15:80'
}

try:
    # Send a GET request with proxies
    response = requests.get(url, headers=headers, proxies=proxies, verify=False)

    # Check if request was successful
    if response.status_code == 200:
        print("200 OK")
        print(response.text)
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())

    #     ip = soup.find('div', class_='ip').text.strip()
    #     location = soup.find('div', class_='value-country').text.strip()
    #     print(f'IP: {ip}\nLocation: {location}')
    else:
        print('Request failed:', response.status_code)
except Exception as e:
    print('An error occurred:', str(e))


# import requests
# from bs4 import BeautifulSoup
# import ssl
# # from urllib.request import certifi
# import socks
# import socket
# from urllib.request import urlopen
#
# with open("valid_proxies.txt", "r") as f:
#     proxies = f.read().splitlines()
#
#
#
#
# # socks.setdefaultproxy(socks.SOCKS5, 'localhost', 9150)
# # socket.socket = socks.socksocket
# # print(urlopen('').read())
#
# headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'
# }
#
# # proxies = {
# #     'https': 'http://127.0.0.1:1080'
# # }
# #
# def get_location(url):
#     response = requests.get(url, headers=headers, proxies={'http': '52.16.232.164:3128', 'https': '54.248.238.110:80'})
#     soup = BeautifulSoup(response.text, 'lxml')
#
#     ip = soup.find('div', class_='ip').text.strip()
#     location = soup.find('div', class_='value-country').text.strip()
#     print(f'IP: {ip}\nLocation: {location}')
#
# def main():
#     get_location(url='https://2ip.ru')
#
# if __name__ == '__main__':
#     main()
#


# import matplotlib.pyplot as plt
# import pandas as pd
#
# data = {
#     'Дата': pd.date_range(start='2024-03-01', end='2024-03-30'),
#     'Bitcoin': [50000, 52000, 54000, 53000, 55000, 56000, 57000, 59000, 60000, 61000, 62000, 63000, 64000, 65000, 66000, 67000, 66000, 67000, 68000, 69000, 70000, 71000, 72000, 73000, 74000, 75000, 76000, 77000, 78000, 79000],
#     'Ethereum': [2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450]
# }
#
# df = pd.DataFrame(data)
# df.set_index('Дата', inplace=True)
#
# plt.figure(figsize=(10, 6))
# plt.plot(df.index, df['Bitcoin'], label='Bitcoin', marker='o')
# plt.plot(df.index, df['Ethereum'], label='Ethereum', marker='o')
#
# plt.title('Динамика цен на Bitcoin и Ethereum за месяц')
# plt.xlabel('Дата')
# plt.ylabel('Цена (USD)')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.legend()
#
# plt.tight_layout()
# plt.show()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Firefox()
# driver.get('https://www.example.com')
# res = driver.find_element(By.TAG_NAME, 'h1')
# print(res.text)
# driver.implicitly_wait(10)
# driver.close()

# from lxml import etree
# html_string = "<html><body><h1>Привет, мир!</h1></body></html>"
# root = etree.fromstring(html_string)
# el = root.find(".//h1")
# print(el.text)

# import requests
# r = requests.get('https://www.example.com')
# print(r)

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("https://www.example.com")
# bsObj = BeautifulSoup(html)
# print(bsObj.get_text())

# from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
#
# url = "https://www.example.com/nonexistent_page"
#
# try:
#     response = urlopen(url)
# except HTTPError as e:
#     print(f"HTTP Error: {e.code}")
# except URLError as e:
#     print(f"URL Error: {e.reason}")

# from urllib.parse import urlparse
#
# url = "https://www.example.com/search?q=python&amp;lang=en"
# parsed_url = urlparse(url)
#
# print(parsed_url)

# from urllib.request import urlopen
#
# url = "https://www.example.com"
# response = urlopen(url)
#
# print(response.read().decode('utf-8'))

import pymysql
from config_test import *
import psycopg2

# try:
#     connection = psycopg2.connect(database=db_name, user=user, password=password, host=host)
#
#     with connection.cursor() as cursor:
#         create_table_query = "CREATE TABLE public.users(id serial PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))"
#         cursor.execute(create_table_query)
#         connection.commit()
#         # print(cursor.fetchone())
#
# except Exception as e:
#     print(e)
#     print("Something went wrong")
# finally:
#     if connection:
#         connection.close()
#         print("PostgreSQL connection is closed")

# try:
#     connection = pymysql.connect(host=host,
#                              port=3306,
#                              user=user,
#                              password=password,
#                              database=db_name,
#                              cursorclass=pymysql.cursors.DictCursor)
#     print("Connection successful")
#     print("--------------------")

    # try:
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
        #                                  " name varchar(32)," \
        #                              " password varchar(32)," \
        #                              " email varchar(32), PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully")


        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Anna', 'qwerty', 'pochta@abc.de');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     select_all_rows = "SELECT * FROM `users`"
        #     cursor.execute(select_all_rows)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)

        # with connection.cursor() as cursor:
        #     update_query = 'UPDATE `users` SET `password` = %s WHERE `id` = 1'
        #     cursor.execute(update_query, ("password"))
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM users WHERE id = %s"
        #     cursor.execute(delete_query, 1)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     drop_table = "DROP TABLE IF EXISTS `users`"
#
#     finally:
#         connection.close()
# except Exception as e:
#     print(e)
#     print("Connection failed")

# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get('http://pythonscraping.com')
# driver.implicitly_wait(1)
# print(driver.get_cookies())
#
# savedCookies = driver.get_cookies()
#
# driver2 = webdriver.Firefox()
# driver2.get('http://pythonscraping.com')
# driver2.delete_all_cookies()
# for cookie in savedCookies:
#     driver2.add_cookie(cookie)
# driver2.get('http://pythonscraping.com')
# driver2.implicitly_wait(1)
# print(driver2.get_cookies())

