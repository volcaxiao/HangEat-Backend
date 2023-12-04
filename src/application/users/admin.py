from django.contrib import admin

from .models.auth_record import AuthRecord
from .models.email_captcha import EmailCaptcha
from .models.user import User


# Register your models here.
admin.site.register(User)

admin.site.register(EmailCaptcha)

admin.site.register(AuthRecord)
