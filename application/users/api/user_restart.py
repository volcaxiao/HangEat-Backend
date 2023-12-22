"""
关于用户收藏的店铺的api
"""

from .. import *
from .auth import jwt_auth
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from ..models import User, Collection
from ...restaurant.models import Restaurant


@response_wrapper
@jwt_auth()
@require_POST
def collect_restart(request):
    user = request.user
    post_data = parse_data(request)
    target_id = post_data.get('target_id')
    target_restart = Restaurant.objects.filter(id=target_id).first()
    if target_restart is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅不存在！")
    if target_restart in user.collections.all():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "已收藏！")
    user.collections.add(target_restart)
    return success_api_response({"message": "收藏成功！"})


@response_wrapper
@jwt_auth()
@require_POST
def uncollect_restart(request):
    user = request.user
    post_data = parse_data(request)
    target_id = post_data.get('target_id')
    target_restart = Restaurant.objects.filter(id=target_id).first()
    if target_restart is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅不存在！")
    if target_restart not in user.collections.all():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "未收藏！")
    user.collections.remove(target_restart)
    return success_api_response({"message": "取消收藏成功！"})


@response_wrapper
@jwt_auth()
@require_GET
def get_collections_num(request):
    user = request.user
    collections = user.collections.all()
    return success_api_response({"collections_num": collections.count()})


@response_wrapper
@jwt_auth()
@require_GET
def get_collections_list(request):
    user = request.user
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    data = get_query_set_list(user.collections, left, right, ['id', 'name', 'img', 'creator', 'tags'])
    return success_api_response(data)
