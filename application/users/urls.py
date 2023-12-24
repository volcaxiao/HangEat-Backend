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
    path('get-user-info/<int:user_id>', get_user_info_by_id),

    path('refresh-token', refresh_token),
    # email
    path('send-captcha', send_captcha),
    path('change-email', change_email),
    # user&user
    path('subscribe', subscribe),
    path('unsubscribe', unsubscribe),
    path('get-subscriptions-num', get_subscriptions_num),
    path('get-subscriptions-list', get_subscriptions_list),
    path('get-subscribers-num', get_subscribers_num),
    path('get-subscribers-list', get_subscribers_list),
    path('get-relation-between', get_relation_between),
    # user&restart
    path('collect', collect_restart),
    path('uncollect', uncollect_restart),
    path('get-collections-num', get_collections_num),
    path('get-collections-list', get_collections_list),
]
