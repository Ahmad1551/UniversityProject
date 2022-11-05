from django.db import models

from config.mixins import TimeStampedModel


class Organization(TimeStampedModel):
    image = models.ImageField(upload_to='organizations', null=True, blank=True)
    name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, null=True, blank=True)
    about_link = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


#products/models.py
class Product(TimeStampedModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    name = models.CharField(max_length=200)
    plan_description = models.CharField(max_length=500, help_text='Duration, Quality eg. 1 Month, 720p, 5K Views')
    description = models.TextField(null=True, blank=True, help_text='Description of the product')
    original_price = models.PositiveIntegerField(help_text='Market Price(USD), eg. 100')
    seller_price = models.PositiveIntegerField(help_text='Price you are selling at(USD), eg. 50')
    quantity = models.PositiveIntegerField(help_text='Number of products available')
    image = models.ImageField(upload_to='products/')

    is_available = models.BooleanField(default=False, help_text='Is the product available for sale?')

    def discount(self):
        if self.original_price and self.seller_price:
            return int((self.original_price - self.seller_price) / self.original_price * 100)
        return 0

    def __str__(self):
        return self.name
