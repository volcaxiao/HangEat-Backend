"""
restaurant model
"""
from django.db import models
from .address import Address


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    img = models.ImageField(upload_to='restaurant/', default='restaurant/default.png', verbose_name='店铺图像')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creater = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag')


    def __str__(self):
        return self.name