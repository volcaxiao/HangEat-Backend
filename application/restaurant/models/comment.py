"""
用户发布的餐馆帖子下的评论
"""

from django.db import models


class Comment(models.Model):
    content = models.CharField(max_length=200)
    comment_time = models.DateTimeField(auto_now_add=True)

    refer_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)

    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')

    agrees = models.ManyToManyField('users.User', related_name='agreedComments')

    def __str__(self):
        return self.comment_content