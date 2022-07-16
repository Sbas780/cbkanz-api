from bs4 import BeautifulSoup
import requests
import re
from .utils import findPriceInString


def get_daily_clack_products(link, type):
    text_request = requests.get(link).text
    soup = BeautifulSoup(text_request, 'lxml')
    items = soup.findAll('product-item', class_="product-item")
    product_list = []
    for item in items:
        is_on_sale = False
        href = item.find('a', class_="product-item__aspect-ratio aspect-ratio aspect-ratio--short", href=True)
        product_href = "https://dailyclack.com" + href['href']
        title = item.find('a', class_="product-item-meta__title").text
        prices = item.find('div', class_="price-list price-list--centered")
        current_price = findPriceInString(item.find('span', class_='price').text)[0]
        regular_price = None
        try:
            regular_price = findPriceInString(item.find('span', class_='price price--compare').text)[0]
            is_on_sale = True
        except:
            pass

        product_list.append({"product_title": title,
                             "product_href": product_href,
                             "current_prices": current_price,
                             "is_on_sale": is_on_sale,
                             "regular_price": regular_price,
                             "type": type,
                             "vendor": "Daily Clack"
                             })

    return product_list


def daily_clack_product_handler():
    LINK = "https://dailyclack.com/collections"
    PRODUCT_TYPE = ["keycaps", "switches", "keyboards", "deskmats", "stabilisers"]

    product_list = []
    page_count = 1
    for type in PRODUCT_TYPE:
        next_page = True
        while next_page:
            x = (get_daily_clack_products(f'https://dailyclack.com/collections/{type}?page={page_count}', type))
            product_list.append(x)
            page_count += 1
            if len(x) == 0:
                page_count = 1
                next_page = False
    return product_list



