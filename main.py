from bs4 import BeautifulSoup
import requests

#fetch data from websites
#todo: scraping product name and prize, returning the data
def scrape_morele(query, number):
    response = requests.get('https://www.morele.net/wyszukiwarka/?q={query}')
def scrape_ceneo(query, number):
    response = requests.get('https://www.ceneo.pl/;szukaj-{query}?nocatnarrow=1')
def scrape_mediaexpert(query, number):
    response = requests.get('https://www.mediaexpert.pl/search?query[menu_item]=&query[querystring]={query}')
def scrape_mediamarkt(query, number):
    response = requests.get('https://mediamarkt.pl/search?query%5Bmenu_item%5D=&query%5Bquerystring%5D={query}')
def scrape_eurortv(query, number):
    response = requests.get('https://www.euro.com.pl/search.bhtml?keyword={query}')

#todo: either gui or console