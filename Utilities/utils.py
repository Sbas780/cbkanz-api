import re
from .daily_clack import get_daily_clack_products



def findPriceInString(string):
    price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)', string)
    return price


def handle_products():
    pass