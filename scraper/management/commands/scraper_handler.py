from django.core.management.base import BaseCommand
from Utilities.daily_clack import get_daily_clack_products, daily_clack_product_handler
from Utilities.utils import findPriceInString
from scraper.models import Product, Vendor



class Command(BaseCommand):
    help = 'Run the scrapper functions'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        product_list = daily_clack_product_handler()
        final_products = []


        for product in product_list:
            for p in product:
                vendor_id = Vendor.objects.get(vendor_name='Daily Clack').pk
                Product.objects.create(product_title=p['product_title'],
                                       product_url=p['product_href'],
                                       product_price=p['current_prices'],
                                       product_isOnSale=p['is_on_sale'],
                                       # product_salePrice=p['regular_price'],
                                       product_type=p['type'],
                                       product_vendor_id=vendor_id)

        print("Done..")

