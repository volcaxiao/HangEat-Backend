"""
用户消息的模型
"""

from django.db import models


class Message(models.Model):
    sender = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='receiver')
    content = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    isRead = models.BooleanField(default=False)
