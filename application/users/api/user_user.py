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
from ..models import User
from ..models import Message


@response_wrapper
@jwt_auth()
@require_POST
def subscribe(request):
    user = request.user
    target_id = request.POST.get('target_id')
    target_user = User.objects.filter(id=target_id).first()
    if target_user is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "用户不存在！")
    if int(target_id) == int(user.id):
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "不能关注自己！")
    if target_user in user.subscribes.all():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "已关注！")
    user.subscribes.add(target_user)
    return success_api_response({"message": "关注成功！"})


@response_wrapper
@jwt_auth()
@require_POST
def unsubscribe(request):
    user = request.user
    target_id = request.POST.get('target_id')
    target_user = User.objects.filter(id=target_id).first()
    if target_user is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "用户不存在！")
    if int(target_id) == int(user.id):
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "不能取关自己！")
    if target_user not in user.subscribes.all():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "未关注！")
    user.subscribes.remove(target_user)
    return success_api_response({"message": "取关成功！"})


@response_wrapper
@jwt_auth()
@require_GET
def get_subscribes_num(request):
    user = request.user
    subscribes = user.subscribes.all()
    return success_api_response({"follower_num": subscribes.count()})


@response_wrapper
@jwt_auth()
@require_GET
def get_subscribes(request):
    user = request.user
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    subscribes = user.subscribes.all()
    subscribes_cnt = subscribes.count()
    left = max(0, min(left, right, subscribes_cnt))
    right = min(subscribes_cnt, max(left, right))
    print(left, right)
    print(subscribes)
    subscribes = subscribes[left:right]
    data = {"subscribes_cnt": subscribes_cnt,
            'query_cnt': right - left}
    for follow in subscribes:
        data.update({follow.username: {
            'id': follow.id,
            'username': follow.username,
            'motto': follow.motto,
            'avatar': follow.get_avatar_url(),
        }})
    return success_api_response(data)


@response_wrapper
@jwt_auth()
@require_GET
def get_fans_num(request):
    user = request.user
    fans = user.fans.all()
    return success_api_response({"fans_num": fans.count()})


@response_wrapper
@jwt_auth()
@require_GET
def get_fans(request):
    user = request.user
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    fans = user.fans.all()
    fans_cnt = fans.count()
    left = max(0, min(left, right, fans_cnt))
    right = min(fans_cnt, max(left, right))
    fans = fans[left:right]
    data = {"fans_num": fans_cnt,
            'query_cnt': right - left}
    for fan in fans:
        data.update({fan.username: {
            'id': fan.id,
            'username': fan.username,
            'motto': fan.motto,
            'avatar': fan.get_avatar_url(),
        }})
    return success_api_response(data)


# @response_wrapper
# @jwt_auth()
# @require_POST
# def send_message(request: HttpRequest):
#     user = request.user
#     target_id = request.POST.get('target_id')
#     target_user = User.objects.filter(id=target_id).first()
#     if target_user is None:
#         return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "用户不存在！")
#     if target_user == user:
#         return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "不能给自己发消息！")
#     message = request.POST.get('message')
#     if message is None:
#         return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "消息不能为空！")
#     message = Message.objects.create(sender=user, receiver=target_user, content=message)
#     return success_api_response({"message": "发送成功！"})