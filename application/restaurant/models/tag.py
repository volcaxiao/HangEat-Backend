"""
店铺的tag
"""

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=200, blank=True)
    creator = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
