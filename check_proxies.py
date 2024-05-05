import threading
import queue

import requests

q = queue.Queue()
valid_proxies = []

with open('proxyList.txt', 'r') as f:
    proxies = f.read().splitlines()
    for p in proxies:
        q.put(p)

def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get('http://httpbin.org/get', proxies={'http': proxy, 'https': proxy})
        except:
            continue
        if res.status_code == 200:
            print(proxy)

for _ in range(10):
    threading.Thread(target=check_proxies).start()