from bs4 import BeautifulSoup
import requests
from utils import utils

switch_keys_products = []


def getSwitchKeysProducts(link, type):
    text_request = requests.get(link).text
    soup = BeautifulSoup(text_request, 'lxml')
    items = soup.findAll('div', class_='Grid__Cell 1/2--phone 1/3--tablet-and-up 1/4--lap-and-up')

    for item in items:
        temp_dict = {}
        try:
            href = item.find('a', class_="ProductItem__ImageWrapper ProductItem__ImageWrapper--withAlternateImage",
                             href=True)
            temp_dict["URL"] = "https://www.switchkeys.com.au" + href['href']
        except TypeError:
            href = item.find('a', class_="ProductItem__ImageWrapper",
                             href=True)

            temp_dict["URL"] = "https://www.switchkeys.com.au" + href['href']

        title = item.find('h2', class_="ProductItem__Title Heading").text.strip()
        temp_dict['title'] = title

        try:
            price = item.find('span', class_="ProductItem__Price Price Text--subdued").text.strip()
            temp_dict['regular_price'] = utils.findPriceInString(price)
            temp_dict['sale_price'] = None
            temp_dict['isOnSale'] = False
        except AttributeError:
            sale_price = item.find('span', class_='ProductItem__Price Price Price--highlight Text--subdued'). \
                text.strip()
            regular_price = item.find('span', class_='ProductItem__Price Price Price--compareAt Text--subdued'). \
                text.strip()
            temp_dict['regular_price'] = utils.findPriceInString(regular_price)
            temp_dict['sale_price'] = utils.findPriceInString(sale_price)
            temp_dict['isOnSale'] = True
        temp_dict['type'] = type
        switch_keys_products.append(temp_dict)


getSwitchKeysProducts("https://www.switchkeys.com.au/collections/deskmats", 'keycaps')
for i in switch_keys_products:
    print(i)
