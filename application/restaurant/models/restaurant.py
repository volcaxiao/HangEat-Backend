"""
restaurant model
"""
from django.db import models
from .address import Address
from django.conf import settings


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    detail_addr = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    img = models.ImageField(upload_to='restaurant/', default='restaurant/default.png', verbose_name='店铺图像')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', related_name='restaurants', through='RestaurantTag')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']