import csv
import re
import time
import cloudscraper
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Proxy


def get_source_html(url):
    driver = webdriver.Chrome()
    # driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(5)

        with open("avito_data.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

        time.sleep(5)

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

def get_flats_pages():
    with open("avito_data.html", encoding="utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    all_flat_hrefs = soup.find("div", {"data-marker":"catalog-serp"}).find_all("a", {"data-marker": "item-title"})
    # print(all_flat_hrefs)
    pages = []
    for item in all_flat_hrefs:
        pages.append(item.get("href"))
        # print(item.text + ": " + item.get("href"))
    # print(len(all_flat_hrefs))
    return pages

def get_source_html_for_flat(url):
    # s = cloudscraper.create_scraper(delay=10, browser={'custom': 'ScraperBot/1.0'})
    # params = {
    #     'forceLocation': False,
    #     'locationId': 653040,
    #     'lastStamp': 1683748131,
    #     'limit': 30,
    #     'offset': 89,
    #     'categoryId': 4
    # }
    # r = s.get(url, params=params)
    # print(r)
    driver = webdriver.Chrome()

    try:
        driver.get(url=url)
        time.sleep(1)

        with open("flat_data.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

        time.sleep(1)

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

def get_info(url):
    info = []

    with open("flat_data.html", encoding="utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    try:
        data_1 = soup.find("ul", class_=re.compile("^(params-paramsList)")).find_all("li")
        for item in data_1:
            # print(item.text.split(":"))
            info.append(item.text.split(":"))
    except Exception as _ex:
        print(_ex)
    # print(data_1)

    try:
        data_2 = soup.find("ul", class_=re.compile("^(style-item-params)")).find_all("li")
        for item in data_2:
        # print(str(item.text.split(":")))
            info.append(item.text.split(":"))
    except Exception as _ex:
        print(_ex)

    kitchen_area = "—"
    living_area = "—"
    floor = "—"
    ceiling_height = "—"
    bathroom = "—"
    windows = "—"
    finishing = "—"
    neighbourhood = "—"
    official_developer = "—"
    type_of_boredom = "—"
    date = "—"
    house_type = "—"
    floors_total = "—"
    passenger_elevator = "—"
    service_lift = "—"
    parking = "—"

    for item in info:
        if item[0] == "Количество комнат":
            rooms = item[1]
        elif item[0] == "Общая площадь":
            apartment_area = item[1]
        elif item[0] == "Площадь кухни":
            kitchen_area = item[1]
        elif item[0] == "Жилая площадь":
            living_area = item[1]
        elif item[0] == "Этаж":
            floor = item[1]
        elif item[0] == "Высота потолков":
            ceiling_height = item[1]
        elif item[0] == "Санузел":
            bathroom = item[1]
        elif item[0] == "Окна":
            windows = item[1]
        elif item[0] == "Отделка":
            finishing = item[1]
        elif item[0] == "Название новостройки":
            neighbourhood = item[1]
        elif item[0] == "Официальный застройщик":
            official_developer = item[1]
        elif item[0] == "Тип участия":
            type_of_boredom = item[1]
        elif item[0] == "Срок сдачи":
            date = item[1]
        elif item[0] == "Тип дома":
            house_type = item[1]
        elif item[0] == "Этажей в доме":
            floors_total = item[1]
        elif item[0] == "Пассажирский лифт":
            passenger_elevator = item[1]
        elif item[0] == "Грузовой лифт":
            service_lift = item[1]
        elif item[0] == "Парковка":
            parking = item[1]


        # print(item)
    # if (address)
    address = soup.find("div", {"itemprop":"address"}).find("span").text
    # print(address)

    metro = soup.find("div", {"itemprop":"address"}).text.replace(address, "").replace(".", ", ")
    # print(metro)

    price = soup.find("span", {"itemprop":"price"}).get("content")
    # print(price)

    with open("apartments_table.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                url,
                rooms,
                metro,
                address,
                price,
                kitchen_area,
                living_area,
                floor,
                ceiling_height,
                bathroom,
                windows,
                finishing,
                neighbourhood,
                official_developer,
                type_of_boredom,
                date,
                house_type,
                floors_total,
                passenger_elevator,
                service_lift,
                parking
            )
        )



def main():
    with open("apartments_table.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow((
                "Ссылка",
                "Количество комнат",
                "Метро",
                "Адрес",
                "Цена",
                "Площадь кухни",
                "Жилая площадь",
                "Этаж",
                "Высота потолков",
                "Санузел",
                "Окна",
                "Отделка",
                "Название новостройки",
                "Официальный застройщик",
                "Тип участия",
                "Срок сдачи",
                "Тип дома",
                "Этажей в доме",
                "Пассажирский лифт",
                "Грузовой лифт",
                "Парковка"
            )
        )
    for i in range(10  , 12):
        get_source_html(f"https://www.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?p={i}")
        flats_pages = get_flats_pages()

        for flat in flats_pages:
            get_source_html_for_flat("https://www.avito.ru" + str(flat))
            get_info(str(flat))


if __name__ == "__main__":
    main()
