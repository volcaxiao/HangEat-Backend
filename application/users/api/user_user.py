"""
关于用户与用户之间交互的api
    1. 关注
    2. 取关
    3. 获取关注列表
    4. 获取粉丝列表

    5. 发消息
    6. 发送图片
"""
from django.http import HttpRequest

from .. import *
from .auth import jwt_auth
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from ..models import User, Subscribe
from ..models import Message


@response_wrapper
@jwt_auth()
@require_POST
def subscribe(request):
    user = request.user
    post_data = parse_data(request)
    target_id = post_data.get('target_id')
    target_user = User.objects.filter(id=target_id).first()
    if target_user is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "用户不存在！")
    if int(target_id) == int(user.id):
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "不能关注自己！")
    if target_user in user.subscriptions.all():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "已关注！")
    user.subscriptions.add(target_user)
    return success_api_response({"message": "关注成功！"})


@response_wrapper
@jwt_auth()
@require_POST
def unsubscribe(request):
    user = request.user
    post_data = parse_data(request)
    target_id = post_data.get('target_id')
    target_user = User.objects.filter(id=target_id).first()
    if target_user is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "用户不存在！")
    if int(target_id) == int(user.id):
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "不能取关自己！")
    if target_user not in user.subscriptions.all():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "未关注！")
    user.subscriptions.remove(target_user)
    return success_api_response({"message": "取关成功！"})


@response_wrapper
@jwt_auth()
@require_GET
def get_subscriptions_num(request):
    user = request.user
    subscribes = user.subscriptions.all()
    return success_api_response({"subscriptions_num": subscribes.count()})


@response_wrapper
@jwt_auth()
@require_GET
def get_subscriptions_list(request):
    user = request.user
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    data = get_query_set_list(user.subscriptions, left, right, ['id', 'username', 'motto', 'avatar'])
    for item in data['list']:
        is_mutual = user.subscriptions.filter(id=item['id']).first().subscriptions.filter(id=user.id).exists()
        item['is_mutual'] = is_mutual
    return success_api_response(data)


@response_wrapper
@jwt_auth()
@require_GET
def get_subscribers_num(request):
    user = request.user
    fans = user.subscribers.all()
    return success_api_response({"subscribers_num": fans.count()})


@response_wrapper
@jwt_auth()
@require_GET
def get_subscribers_list(request):
    user = request.user
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    data = get_query_set_list(user.subscribers, left, right, ['id', 'username', 'motto', 'avatar'])
    for item in data['list']:
        is_mutual = user.subscribers.filter(id=item['id']).first().subscribers.filter(id=user.id).exists()
        item['is_mutual'] = is_mutual
    return success_api_response(data)


@response_wrapper
@jwt_auth()
@require_GET
def get_relation_between(request: HttpRequest):
    user1 = request.GET.get('user1')
    user2 = request.GET.get('user2')

    user1 = User.objects.filter(id=user1).first()
    user2 = User.objects.filter(id=user2).first()

    if user1 and user2:
        res = {'1subscribe2': True if user1.subscriptions.filter(id=user2.id).exists() else False,
               '2subscribe1': True if user2.subscriptions.filter(id=user1.id).exists() else False}
        return success_api_response(res)

    return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "用户不存在！")
