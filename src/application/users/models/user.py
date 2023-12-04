"""
这是储存用户基本信息的模型
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


MEDIA_ADDRESS = 'http://103.133.178.116:8000/media/'


class User(AbstractUser):
    gender_choices = (
        ('secret', '不设置/保密'),
        ('male', '男'),
        ('female', '女'),
    )

    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='用户ID', editable=False)
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(unique=True, verbose_name='邮箱', error_messages={'unique': '该邮箱已被注册'}, blank=False)
    gender = models.CharField(choices=gender_choices, max_length=32, default='保密', verbose_name='性别')
    motto = models.CharField(max_length=256, default='这个人很懒，什么都没有留下', verbose_name='个性签名')
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', default='avatar/default.png', verbose_name='头像')

    def get_avatar_url(self):
        return MEDIA_ADDRESS + str(self.avatar)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-date_joined']
        verbose_name = '用户'
        verbose_name_plural = '用户'
