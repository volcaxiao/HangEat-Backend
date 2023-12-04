from django.db import models

# 存储用户自定义的知识图谱


class UserGraphNode(models.Model):  # 节点
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    father = models.CharField(max_length=255)   # 父节点编号
    node_name = models.CharField(max_length=255)  # 节点名字
    node_id = models.CharField(max_length=255)
