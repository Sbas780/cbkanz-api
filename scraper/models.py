from django.db import models


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=250)
    vendor_url = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.vendor_name


class Product(models.Model):
    product_title = models.CharField(max_length=250)
    product_url = models.CharField(max_length=250)
    product_price = models.FloatField()
    product_isOnSale = models.BooleanField(default=False)
    product_salePrice = models.FloatField(null=True, blank=True)
    product_type = models.CharField(max_length=250)
    product_image = models.ImageField()
    product_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_title
