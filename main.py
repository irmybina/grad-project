import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from auth_config import username, password
import random
import time

options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--proxy-server=194.28.209.178:9407")


driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7", "ru"],
        vendor="Google Inc.",
        platform="Win-32",
        webdriver="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
                   "Safari/537.36",
        fix_hairline=True)

wait = WebDriverWait(driver, 20)


def authorize():
    time.sleep(random.randint(5, 10))

    driver.find_element(By.ID, "login").send_keys(username)
    time.sleep(random.randint(2, 6))

    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(random.randint(2, 4))

    driver.find_element(By.CLASS_NAME, "butred").click()
    time.sleep(random.randint(2, 15))

    driver.find_element(By.XPATH, "//a[@href='/authors.asp']").click()


def handle_captcha():
    print("Checking Captcha...")
    if driver.title == "Тест Тьюринга":
        print("Captcha to be solved")
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
        time.sleep(random.randint(55, 72))

        handle_captcha()
        go_to_next_page_to_scrap()
    else:
        print("No Captcha")


def go_to_page(page):
    print("Going to page " + str(page))
    driver.execute_script("javascript:goto_page(" + str(page) + ")")
    time.sleep(random.randint(5, 10))


def go_to_next_page_to_scrap():
    go_to_page(page_counter)
    time.sleep(6)


def scrap():
    print("Processing scraped page...")
    with open("scrap.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table", {'id': 'restab'})

    rows = table.findAll('tr', {'bgcolor': '#f5f5f5'})

    with open('bot/output.csv', 'a', newline='', encoding='utf-8') as csvfile:
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

    print("Data from page " + str(page_counter) + " saved to output.csv")


url_init = "https://www.google.com/"
page_counter = 685

# запуск драйвера

if __name__ == '__main__':
    print("Start")
    driver.get(url_init)
    time.sleep(15)
    field = driver.find_element(By.XPATH, "//textarea[@title='Поиск']")
    time.sleep(random.randint(5, 10))
    field.send_keys("РИНЦ")
    time.sleep(random.randint(5, 10))
    driver.find_element(By.XPATH, "//input[@name='btnK']").click()
    time.sleep(random.randint(5, 10))
    search = driver.find_element(By.XPATH, "//div[@id='search']")
    search.find_element(By.XPATH, ".//a").click()
    print("FOUND PAGE")

    authorize()

    print("AUTH SUCCESSFUL")
    go_to_next_page_to_scrap()
    while page_counter < 10844:
        handle_captcha()
        if driver.title == "Поиск авторов":
            print("Start scrapping page" + str(page_counter))
            html_source = driver.page_source
            with open("scrap.html", "w", encoding="utf-8") as file:
                file.write(html_source)
            print("Scrapping")
            scrap()
            page_counter += 1
            time.sleep(random.randint(5, 10))
            go_to_next_page_to_scrap()
        else:
            print("Something went wrong...")
            time.sleep(random.randint(120, 170))

    driver.quit()