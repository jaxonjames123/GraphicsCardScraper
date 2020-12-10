from selectorlib import Extractor
import requests
from time import sleep
from url_generator import url_gen
from twilio.rest import Client
from proxy_generator import get_proxies
from itertools import cycle
import traceback
from lxml.html import fromstring
from bs4 import BeautifulSoup


def get_proxies():
    urls = 'https://www.proxy-list.download/api/v1/get?type=https&country=US'
    res = requests.get(urls)
    proxy_list = res.text.split()
    for item in range(len(proxy_list)):
        proxy_list[item] = proxy_list[item].strip()
    return proxy_list


e = Extractor.from_yaml_file('amazon_selectors.yml')
client = Client('ACc731a966a21ff58247aa1c5e4798cd8a', 'ddec7b1f9d9a95bea16f7cd3889752ae')
proxies = get_proxies()
proxy_pool = cycle(proxies)
headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}
url = 'https://www.google.com'
for i in range(1, 11):
    proxy = next(proxy_pool)
    print('\n' + proxy)
    print(f'Request {i}')
    try:
        response = requests.get(url, proxies={"http": 'http://' + str(proxy), "https": 'https://' + str(proxy)})
        print(response.json())
    except IOError:
        # Most free proxies will often get connection errors. You will have retry the entire request using another
        # proxy to work. We will just skip retries as its beyond the scope of this tutorial and we are only
        # downloading a single url
        print("Skipping. Connnection error")


def amazon_scrape(url):
    resp = requests.get(url, proxies=proxies, headers=headers)
    if resp.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in resp.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n" % url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d" % (url, resp.status_code))
        return None
        # Pass the HTML of the page and create
    return e.extract(resp.text)


urls = url_gen()
urls.append(
    'https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS?smid=ATVPDKIKX0DER&pf_rd_r=HRR92YSSKF9KDCJWV7K4&pf_rd_p=03376bed-5c27-4309-89c6-77ada761a5c6&pd_rd_r=764bd818-ec2b-4af7-99d1-256a49a52acc&pd_rd_w=k8wPG&pd_rd_wg=2zWxO&ref_=pd_gw_unk')

# while True:
#     for url in urls:
#         data = amazon_scrape(url)
#         data.update({'name': str(data.get('name'))[0:30]})
#         if data.get('availability') != 'In Stock.':
#             data.update({'availability': 'Out of Stock'})
#         else:
#             client.messages.create(to="+17328414344",
#                                    from_="+15306014261",
#                                    body=f"{data.get('name')} in stock!")
#         if data:
#             print(data)
#             sleep(2)
