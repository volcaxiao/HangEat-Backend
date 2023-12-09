"""
用户发布的餐馆帖子下的评论
"""

from django.db import models


class Comment(models.Model):
    comment_content = models.CharField(max_length=200)
    comment_time = models.DateTimeField(auto_now_add=True)

    refer_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)

    reply_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    agree = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_content