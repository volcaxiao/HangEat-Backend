"""
邮箱验证码模型
"""
from datetime import timedelta

from django.db import models
from django.utils import timezone


class EmailCaptcha(models.Model):
    """
    邮箱验证码模型
    """
    email = models.EmailField(verbose_name='邮箱')
    captcha = models.CharField(max_length=20, verbose_name='验证码')
    send_time = models.DateTimeField(verbose_name='发送时间', auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-send_time']
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}:{}'.format(self.email, self.captcha)

    def is_expired(self):
        if timezone.now() - self.send_time > timedelta(minutes=5):
            return True
        else:
            return False
