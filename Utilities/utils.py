import re




def findPriceInString(string):
    price = re.findall(r'[-+]?(?:\d*\.\d+|\d+)', string)
    return price


def handle_products():
    pass