import random

from django.core.mail import send_mail
from django.views.decorators.http import require_GET, require_POST
from django.core.cache import cache

from .auth import generate_token, jwt_auth
from ..models import User
from django.conf import settings
from .. import *


@response_wrapper
@require_POST
def send_email(request):
    # 获取数据
    post_data = parse_data(request)
    email = post_data.get('email')
    content = post_data.get('content')
    # 检查邮箱是否已存在
    if email and User.objects.filter(email=email).exists():
        # 生成token
        token = generate_token(email)
        # 发送邮件
        send_mail(content, token, settings.EMAIL_HOST_USER, [email])
        return success_api_response({"message": "Email sent successfully."})
    else:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "邮箱不存在！")


def varify_captcha(email, captcha):
    entry = cache.get(email)
    return entry == captcha


@response_wrapper
@require_POST
def send_captcha(request):
    post_data = parse_data(request)
    email = post_data.get('email')
    captcha = '%06d' % random.randint(0, 999999)
    email_title = 'HangEat 验证码'
    email_body = '您的验证码为：' + captcha + '，请在5分钟内输入。'
    send_status = send_mail(email_title, email_body, settings.EMAIL_HOST_USER, [email])
    if send_status:
        cache.set(email, captcha, 300)
        return success_api_response({"message": "邮件发送成功，可能存在一定的延迟，请耐心等待。"})
    else:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "邮件发送失败，请检查邮箱是否正确。")


@response_wrapper
@jwt_auth()
@require_POST
def change_email(request):
    post_data = parse_data(request)
    new_email = post_data.get('email')
    captcha = post_data.get('captcha')
    if User.objects.filter(email=new_email).exists():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "邮箱已注册")
    if varify_captcha(new_email, captcha):
        user = request.user
        user.email = new_email
        user.save()
        return success_api_response({"message": "邮箱修改成功！"})
    else:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "验证码错误！")
