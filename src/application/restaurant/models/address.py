"""
地址模型：用于与api交互
"""

from django.db import models


class Address(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    address_name = models.CharField(max_length=50)
    address_detail = models.CharField(max_length=50)
    display_data = models.CharField(max_length=200)
