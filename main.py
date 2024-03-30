from bs4 import BeautifulSoup
import requests
import pprint as pp

#fetch data from websites
#todo: scraping product name and prize, returning the data
#query = product the user wants to find, number = number of results to display

def scrape_morele(query, number):
    response = requests.get(f'https://www.morele.net/wyszukiwarka/?q={query}')
    soup = BeautifulSoup(response.text, 'html.parser')
    results = {}
    i=0
    for product in soup.findAll('div', attrs={'class': 'cat-product-inside'}):
        if (i>=number):
            break
        name = product.find('div', attrs={'class' : 'cat-product-name'}).find('a').text.strip()
        price = product.find('div', attrs={'class' : 'price-new'}).text.strip()
        results[name] = price
        i+=1
    return results

def scrape_ceneo(query, number):
    response = requests.get(f'https://www.ceneo.pl/;szukaj-{query}?nocatnarrow=1')
    soup = BeautifulSoup(response.text, 'html.parser')
    prices = []
    i=0
    for item in soup.select('.cat-prod-row__body'):
        if (i >= number):
            break
        price = item.select('.value')[0].text
        prices.append(price)
        i+=1
    return prices

def scrape_mediaexpert(query, number):
    response = requests.get('https://www.mediaexpert.pl/search?query[menu_item]=&query[querystring]={query}')
def scrape_mediamarkt(query, number):
    response = requests.get('https://mediamarkt.pl/search?query%5Bmenu_item%5D=&query%5Bquerystring%5D={query}')
def scrape_eurortv(query, number):
    response = requests.get('https://www.euro.com.pl/search.bhtml?keyword={query}')

#main loop
#todo: switch to Tkinter GUI after main functionalities are implemented
print("""
1) Morele
2) Ceneo
3) Media Expert
4) Media Markt
5) Euro RTV AGD
""")

choice = input("Select a website: ").lower() #converting the input to lowercase in order to make if condition shorter
query = input("What do you want to look for? ")
number = int(input("How many results to display? "))

if choice == '1' or choice == 'morele':
    print("Browsing morele.net...")
    pp.pprint(scrape_morele(query, number), width=500) #todo: better formatting
    input()
elif choice == '2' or choice == 'ceneo':
    print("Browsing ceneo.pl...")
    print(scrape_ceneo(query, number))
elif choice == '3' or choice == 'media expert':
    print("Browsing mediaexpert.pl...")
    scrape_mediaexpert(query, number)
elif choice == '4' or choice == 'media markt':
    print("Browsing mediamarkt.pl...")
    scrape_mediamarkt(query, number)
elif choice == '5' or choice == 'euro rtv agd':
    print("Browsing euro.com.pl...")
    scrape_eurortv(query, number)

#todo: displaying the data
#data format: list with nested dictionaries [{product:price}]