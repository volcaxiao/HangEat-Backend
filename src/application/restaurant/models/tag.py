"""
店铺的tag
"""

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200, blank=True)
    creater = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
