import requests
from bs4 import BeautifulSoup
import urllib


def scrape_bad_urls():   
    url = 'https://www.sga.gatech.edu/'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    urls = {}
    for link in soup.find_all('a'):
        if ("http" or "https") in link.get('href'):
            urls[link.get('href')] = str(requests.get(link.get('href')).status_code)

    bad_urls = {}
    for url in urls:
        if urls[url] == "404" or urls[url] == '400':
            bad_urls[url] = urls[url]
    
    return bad_urls


        

