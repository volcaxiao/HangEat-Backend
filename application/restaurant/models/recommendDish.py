"""
帖子和推荐菜之间多对多的联系
"""

from django.db import models


class RecommendDish(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    recommend_time = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=200)
    price = models.FloatField()