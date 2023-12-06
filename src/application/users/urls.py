from django.urls import path

from . import api

urlpatterns = [
    path('login', api.login_user),
    path('signup', api.signup_user),
    path('logout', api.logout_user),
    path('delete', api.delete_user),
    path('update-info', api.update_user),
    path('update-avatar', api.update_avatar),
    path('change-password', api.change_password),
    path('forget-password', api.forget_password),
    path('get-user-info', api.get_user_info),

    path('refresh-token', api.refresh_token),

    path('send-captcha', api.send_captcha),
    path('change-email', api.change_email),
]
