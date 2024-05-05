import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from auth_config import username, password
import random
import time

# настройка драйвера
options = webdriver.ChromeOptions()
# options.add_argument('start-maximized')

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 20)

def authorize():
        time.sleep(random.randint(5, 10))

        driver.find_element(By.ID, "login").send_keys(username)
        time.sleep(random.randint(2,6))

        driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(random.randint(2,4))

        driver.find_element(By.CLASS_NAME, "butred").click()
        time.sleep(random.randint(2,15))

        driver.find_element(By.HREF, "/authors.asp").click()
def handleCaptcha():
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
        # below line will click on the checkbox next to 'I'm not a robot'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
        time.sleep(60)

def goToLastScrappedPage():
        driver.find_element("СТРАНИЦЫ").click()

def scrap():
        with open("scrap.html", "r", encoding="utf-8") as file:
                html_content = file.read()
        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table", {'id': 'restab'})

        rows = table.findAll('tr', {'bgcolor': '#f5f5f5'})

        with open('output.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csvwriter = csv.writer(csvfile)

                for row in rows:
                        cells = row.find_all('td')

                        a = (str)(cells[2]).split('<br/>')

                        name = BeautifulSoup(a[0]).get_text()
                        university = BeautifulSoup(a[1]).get_text()
                        publ = cells[3].get_text()
                        cite = cells[4].get_text()
                        hirsh = cells[5].get_text()

                        row_data = [name, university, publ, cite, hirsh]

                        csvwriter.writerow(row_data)

        print("Data from page saved to output.csv")



stealth(driver,
        languages=["ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7", "ru"],
        vendor = "Google Inc.",
        platform="Win-32",
        webdriver="Intel Inc.",
        renderer= "Intel Iris OpenGL Engine",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        fix_hairline=True)

# url = "https://www.elibrary.ru/defaultx.asp?"
url = "https://www.google.com/recaptcha/api2/demo"
# url = "https://bot.incolumitas.com/"

page_counter = 0

# запуск драйвера

driver.get(url)

authorize()

while page_counter < 10:
        if url.title == "Тест Тьюринга":
                handleCaptcha()
                goToLastScrappedPage()
        # elif url.title == "Поиск Авторов":
        else:
                html_source = driver.page_source
                with open("scrap.html", "w", encoding="utf-8") as file:
                        file.write(html_source)
                # scrap()
                page_counter += 1

# time.sleep(random.randint(5,10))
#
# driver.find_element(By.ID, "login").send_keys(username)
# time.sleep(random.randint(2,6))
#
# driver.find_element(By.ID, "password").send_keys(password)
# time.sleep(random.randint(2,4))
#
# driver.find_element(By.CLASS_NAME, "butred").click()
# time.sleep(random.randint(2,15))
#
# driver.find_element(By.HREF, "/authors.asp").click()

# el1 = driver.find_element(By.NAME, "a-1oggnlvchg6q")
# ActionChains(driver).move_to_element(el1).perform()
# time.sleep(2)
# el2 =
# ActionChains(driver).move_to_element(el2).perform()
# el2.click()
# time.sleep(3)
# wait = WebDriverWait(driver, 20)
# wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
# below line will click on the checkbox next to 'I'm not a robot'
# wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
# driver.find_element(By.ID, "recaptcha-demo-submit").click()
# time.sleep(50)
#
# driver.find_element(By.XPATH, "//input[@id='recaptcha-demo-submit']").click()
# el2 = driver.find_element(By.ID, "a636222")
# ActionChains(driver).move_to_element(el2).perform()
#
# time.sleep(20)


# driver.find_element("name", "username").send_keys(username)
# driver.find_element("name", "password").send_keys(password)
#
# driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()
# time.sleep(20)
driver.quit()