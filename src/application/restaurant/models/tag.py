"""
店铺的tag
"""

from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    tag_description = models.CharField(max_length=200)
    creater = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tag_name