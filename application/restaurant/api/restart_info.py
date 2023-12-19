"""
关于餐厅信息的API
    1. 创建餐厅
    2. 获取餐厅信息
    3. 获取餐厅列表
    4. 修改餐厅信息
    5. 删除餐厅
"""
from django.http import HttpRequest
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .. import *
from ..models import Restaurant
from application.users.api.auth import jwt_auth


@response_wrapper
@jwt_auth()
@require_POST
def creat_restaurant(request):
    user = request.user
    post_data = parse_data(request)
    name = post_data.get('name')
    detail_addr = post_data.get('address')
    phone = post_data.get('phone')
    if Restaurant.objects.filter(name=name).exists():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅已存在！")

    if name == 'default':
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "非法取名")

    restart = Restaurant(name=name, creator=user, detail_addr=detail_addr)

    if phone is not None:
        restart.phone = phone

    restart.save()
    return success_api_response({"message": "创建成功！"})


@response_wrapper
@jwt_auth()
@require_http_methods(['PUT'])
def update_restaurant(request: HttpRequest, restart_id: int):
    restart = Restaurant.objects.get(id=restart_id)
    if restart is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    if restart.creator != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '无权修改')
    put_data = parse_data(request)
    name = put_data.get('name')
    description = put_data.get('description')
    detail_addr = put_data.get('address')
    phone = put_data.get('phone')
    if name == 'default':
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "非法取名")
    if Restaurant.objects.filter(name=name).exists():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅已存在！")
    if name is not None:
        restart.name = name
    if description is not None:
        restart.description = description
    if detail_addr is not None:
        restart.detail_addr = detail_addr
    if phone is not None:
        restart.phone = phone
    restart.save()
    return success_api_response({"message": "修改成功！"})


@response_wrapper
@jwt_auth()
@require_POST
def update_image(request: HttpRequest, restart_id: int):
    restart = Restaurant.objects.get(id=restart_id)
    if restart is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    if restart.creator != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '无权修改')
    img = request.FILES.getlist('image')[0] if len(request.FILES.getlist('image')) > 0 else None
    if img is not None:
        if img.size > 1024 * 1024 * 2:
            return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片大小不能超过2MB")
        img.name = restart.name + '.png'
        restart.img = img
    restart.save()
    return success_api_response({"message": "修改成功！"})


@response_wrapper
@require_GET
def get_restaurant_detail(request: HttpRequest, restart_id: int):
    restart = Restaurant.objects.get(id=restart_id)
    if restart is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    detail = model_to_dict(restart)
    return success_api_response(detail)


@response_wrapper
@require_GET
def get_restaurant_num(request: HttpRequest):
    creator_id = request.GET.get('creator_id')
    if creator_id is not None:
        restart_cnt = Restaurant.objects.filter(creator_id=creator_id).count()
    else:
        restart_cnt = Restaurant.objects.count()
    return success_api_response({'restaurant_num': restart_cnt})


@response_wrapper
@require_GET
def get_restaurant_list(request):
    creator_id = request.GET.get('creator_id')
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    if creator_id is not None:
        restaurant_set = Restaurant.objects.filter(creator_id=creator_id)
    else:
        restaurant_set = Restaurant.objects
    data = get_query_set_list(restaurant_set, left, right, ['id', 'name', 'img', 'creator', 'tags'])
    return success_api_response(data)


@response_wrapper
@jwt_auth()
@require_http_methods(['DELETE'])
def delete_restaurant(request: HttpRequest, restart_id: int):
    restart = Restaurant.objects.get(id=restart_id)
    if restart is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    if restart.creator != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '无权删除')
    restart.delete()
    return success_api_response({"message": "删除成功！"})
