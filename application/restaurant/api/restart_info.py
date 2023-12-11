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
    name = request.POST.get('name')
    if Restaurant.objects.filter(name=name).exists():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅已存在！")

    detail_addr = request.POST.get('address')
    restart = Restaurant(name=name, creater=user, detail_addr=detail_addr)

    phone = request.POST.get('phone')
    if phone is not None:
        restart.phone = phone

    img = request.FILES.getlist('avatar')[0] if len(request.FILES.getlist('avatar')) > 0 else None
    if img is not None:
        if img.size > 1024 * 1024 * 2:
            return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片大小不能超过2MB")
        if name == 'default':
            return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "非法取名")
        img.name = name + '.png'
        restart.img = img
    restart.save()
    return success_api_response({"message": "创建成功！"})


@response_wrapper
@jwt_auth()
@require_GET
def get_restaurant_detail(request: HttpRequest, restart_id: int):
    restart = Restaurant.objects.get(id=restart_id)
    if restart is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    detail = model_to_dict(restart)
    return success_api_response(detail)


@response_wrapper
@jwt_auth()
@require_GET
def get_restaurant_num(request: HttpRequest):
    restart_cnt = Restaurant.objects.count()
    return success_api_response({'restaurant_num': restart_cnt})


@response_wrapper
@jwt_auth()
@require_GET
def get_restaurant_list(request):
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    data = get_query_set_list(Restaurant.objects, left, right, ['id', 'name', 'img', 'creater', 'tags'])
    return success_api_response(data)


@response_wrapper
@jwt_auth()
@require_GET
def get_restaurant_num_by_creater(request):
    creater_id = request.GET.get('creater_id')
    restart_cnt = Restaurant.objects.filter(creater_id=creater_id).count()
    return success_api_response({'restaurant_num': restart_cnt})


@response_wrapper
@jwt_auth()
@require_GET
def get_restaurant_list_by_creater(request):
    creater_id = request.GET.get('creater_id')
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    data = get_query_set_list(Restaurant.objects.filter(creater_id=creater_id), left, right, ['id', 'name', 'img', 'creater', 'tags'])
    return success_api_response(data)


@response_wrapper
@jwt_auth()
@require_http_methods(['PUT'])
def edit_restaurant(request: HttpRequest, restart_id: int):
    restart = Restaurant.objects.get(id=restart_id)
    if restart is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    if restart.creater != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '无权修改')
    name = request.POST.get('name')
    description = request.POST.get('description')
    detail_addr = request.POST.get('address')
    phone = request.POST.get('phone')
    img = request.FILES.getlist('avatar')[0] if len(request.FILES.getlist('avatar')) > 0 else None
    if name is not None:
        restart.name = name
    if description is not None:
        restart.description = description
    if detail_addr is not None:
        restart.detail_addr = detail_addr
    if phone is not None:
        restart.phone = phone
    if img is not None:
        if img.size > 1024 * 1024 * 2:
            return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片大小不能超过2MB")
        if name == 'default':
            return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "非法取名")
        img.name = name + '.png'
        restart.img = img
    restart.save()
    return success_api_response({"message": "修改成功！"})


@response_wrapper
@jwt_auth()
@require_POST
def delete_restaurant(request: HttpRequest, restart_id: int):
    restart = Restaurant.objects.get(id=restart_id)
    if restart is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    if restart.creater != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '无权删除')
    restart.delete()
    return success_api_response({"message": "删除成功！"})
