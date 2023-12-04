"""
这是用户收藏夹的 model
"""
from django.db import models


class Favorite(models.Model):
    objects = models.Manager()
    course_id = models.IntegerField()      # 此 id 应当是 video 在 neo4j 数据库中的id
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
