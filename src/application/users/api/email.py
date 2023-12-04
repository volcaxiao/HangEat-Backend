import random

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from auth import generate_token, jwt_auth
from ..models import User
from ..models.email_captcha import EmailCaptcha
from django.conf import settings


def send_email(request):
    if request.method == 'POST':
        # 获取数据
        email = request.POST.get('email')
        # 检查邮箱是否已存在
        if email and User.objects.filter(email=email).exists():
            # 生成token
            token = generate_token(email)
            # 发送邮件
            send_mail()
            return JsonResponse({"message": "Email sent successfully."})
        else:
            return JsonResponse({"error": "Email does not exist."}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)


def varify_captcha(email, captcha):
    entrys = EmailCaptcha.objects.filter(email=email, captcha=captcha)
    varify = False
    for entry in entrys:
        if not entry.is_expired():
            varify = True
            break

    entrys.delete()

    return varify


@require_POST
def send_captcha(request):
    email = request.POST.get('email')
    captcha = '%06d' % random.randint(0, 999999)
    email_title = 'HangEat 验证码'
    email_body = '您的验证码为：' + captcha + '，请在5分钟内输入。'
    send_status = send_mail(email_title, email_body, settings.EMAIL_HOST_USER, [email])
    if send_status:
        entry = EmailCaptcha(email=email, captcha=captcha)
        entry.save()
        return JsonResponse({"message": "邮件发送成功，可能存在一定的延迟，请耐心等待。"})
    else:
        return JsonResponse({"error": "邮件发送失败"}, status=400)


@jwt_auth()
@require_POST
def change_email(request):
    new_email = request.POST.get('email')
    captcha = request.POST.get('captcha')
    print(new_email, captcha)
    if User.objects.filter(email=new_email).exists():
        return JsonResponse({"error": "邮箱已注册！"}, status=400)
    if varify_captcha(new_email, captcha):
        user = request.user
        user.email = new_email
        user.save()
        return JsonResponse({"message": "邮箱修改成功！"})
    else:
        return JsonResponse({"error": "验证码无效"}, status=400)