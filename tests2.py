# 1. Set User-Agent Header: The User-Agent header identifies the browser and operating system used by the client.
# Set a User-Agent header that matches a popular web browser to make your requests appear more like those from a real user's browser.
# You can find common User-Agent strings online or generate one dynamically.
import requests
from bs4 import BeautifulSoup

url = "https://www.elibrary.ru/defaultx.asp?"

proxies = {
    # # 'http': 'http://username:password@proxy_ip:proxy_port',
    # 'https': 'https://www.18.223.25.15:80'
    # 'http': 'http://45.95.147.106:8080',
    'https': 'http://afQEKq:cS4Hdb@213.166.72.159:9822'
}

headers = {
    "USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "ACCEPT":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "ACCEPT-LANGUAGE":"ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "ACCEPT-ENCODING":"gzip, deflate, br"
}
#
# 2. Use Session: Use a session object (requests.Session()) to persist cookies across multiple requests. This simulates a user session and maintains state between requests, such as logged-in status or session-specific data.
session = requests.Session()
session.proxies = proxies
#
# 3. Handle Cookies: Ensure that you handle cookies appropriately, especially if the website requires authentication. Maintain and send cookies with each request to simulate a logged-in user's behavior.

# Simulate a login request and capture cookies
login_data = {
    'username': 'your_username',
    'password': 'your_password'
}
# login_url = 'https://www.2ip.ru'
response = session.post(url) #, data=login_data

# Check if login was successful (check response status code, content, etc.)

# Get cookies from the session
cookies = session.cookies.get_dict()
# print(cookies)
# Make subsequent requests with cookies
# url = 'https://www.2ip.ru'
# response = session.get(url, cookies=cookies)
# print(response.text)

try:
    # Send a GET request with proxies
    response = session.get(url)

    # Check if request was successful
    if response.status_code == 200:
        print("200 OK")
        print(response.text)
        # print(response.text)
        # Parse HTML content
        # soup = BeautifulSoup(response.text, 'lxml')
        # # print(soup.prettify())
        # ip = soup.find('div', class_='ip').text.strip()
        # location = soup.find('div', class_='value-country').text.strip()
        # print(f'IP: {ip}\nLocation: {location}')
    else:
        print('Request failed:', response.status_code)
except Exception as e:
    print('An error occurred:', str(e))



# 4. Emulate Delays: Introduce random delays between requests to simulate human-like browsing behavior. Humans don't typically browse web pages at a constant rate, so adding random delays can help avoid triggering rate-limiting or anti-scraping measures.
#
# 5. Interact with JavaScript: Many modern websites use JavaScript to render content dynamically. If the website relies heavily on JavaScript, consider using a headless browser automation tool like Selenium to interact with the website and scrape dynamically loaded content.
#
# 6. Randomize IP Addresses: Rotate IP addresses or use a pool of proxies to make requests from different IP addresses. This can help prevent IP-based blocking or rate-limiting by the website.
#
# 7. Follow Links: When scraping multiple pages, simulate the behavior of clicking on links or navigating through pagination by following links in the scraped content. This helps mimic a user browsing through the website.
#
# 8. Limit Request Rate: Avoid making too many requests in a short period. Spread out your requests over time to avoid overloading the website's servers and to appear more like a human user.
#
# 9. Handle Captchas and Anti-Bot Measures: Some websites employ CAPTCHA challenges or other anti-bot measures. Implement logic to handle these challenges programmatically if encountered during scraping.


session.close()