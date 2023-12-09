from django.urls import path

from .api import *

urlpatterns = [
    path('login', login_user),
    path('signup', signup_user),
    path('logout', logout_user),
    path('delete', delete_user),
    path('update-info', update_user),
    path('update-avatar', update_avatar),
    path('change-password', change_password),
    path('forget-password', forget_password),
    path('get-user-info', get_user_info),

    path('refresh-token', refresh_token),

    path('send-captcha', send_captcha),
    path('change-email', change_email),

    path('subscribe', subscribe),
    path('unsubscribe', unsubscribe),
    path('get-subscribes', get_subscribes),
    path('get-fans', get_fans),

]
