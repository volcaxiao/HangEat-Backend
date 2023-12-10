"""
用户推荐菜品的模型
"""

from django.db import models


class Dish(models.Model):
    dish_name = models.CharField(max_length=20)
    dish_description = models.CharField(max_length=200)
    dish_price = models.FloatField()
    dish_img = models.ImageField(upload_to='dish/', default='dish/default.png', verbose_name='菜品图像')

    def __str__(self):
        return self.dish_name
