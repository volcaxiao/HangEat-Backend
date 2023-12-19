"""
这是储存用户基本信息的模型
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


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
    avatar = models.ImageField(upload_to='avatar/', default='avatar/default.png', verbose_name='头像')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    last_login = models.DateTimeField(auto_now=True, verbose_name='最后登录时间')
    last_ip = models.GenericIPAddressField(verbose_name='最后登录IP', blank=True, null=True)

    subscriptions = models.ManyToManyField('self', symmetrical=False, related_name='subscribers', through='Subscribe')
    send_messages = models.ManyToManyField('self', symmetrical=False, related_name='received_by', through='Message')
    collections = models.ManyToManyField('restaurant.Restaurant', related_name='collectors', through='Collection')

    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-date_joined']
        verbose_name = '用户'
        verbose_name_plural = '用户'
