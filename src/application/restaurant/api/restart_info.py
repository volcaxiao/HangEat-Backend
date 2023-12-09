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
from src.application.users.api.auth import jwt_auth


@response_wrapper
@jwt_auth()
@require_POST
def creat_restaurant(request):
    user = request.user
    name = request.POST.get('name')
    detail_addr = request.POST.get('address')
    phone = request.POST.get('phone')
    img = request.FILES.getlist('avatar')[0]
    if Restaurant.objects.filter(name=name).exists():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅已存在！")
    if img.size > 1024 * 1024 * 2:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片大小不能超过2MB")
    if name == 'default':
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "非法取名")
    img.name = name + '.png'
    Restaurant.objects.create(name=name, phone=phone, detail_addr=detail_addr, img=img, creater=user)
    return success_api_response({"message": "创建成功！"})


@response_wrapper
@jwt_auth()
@require_GET
def get_restaurant_detail(request: HttpRequest, restart_id: int):
    restart = Restaurant.objects.get(id=restart_id)
    if restart is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    detail = {'name': restart.name,
              'description': restart.description,
              'detail_addr': restart.detail_addr,
              'referrer': restart.creater.name,
              'img_url': restart.get_img_url(),
              'phone': restart.phone,
              }
    tags_name = []
    for tag in restart.tags:
        tags_name.append(tag.tag_name)
    detail.update({'tags': tags_name})
    return success_api_response(detail)


@response_wrapper
@jwt_auth()
@require_GET
def get_restaurant_list(request):
    restart_cnt = Restaurant.objects.count()
    restart_all = Restaurant.objects.all()
    restart_list = []
    for restart in restart_all:
        restart_intro = {
            'id': restart.id,
            'name': restart.name,
            'referer': restart.creater.name,
            'img_url': restart.get_img_url()
        }
        tags_name = []
        for tag in restart.tags:
            tags_name.append(tag.tag_name)
        restart_intro.update({'tags': tags_name})
        restart_list.append(restart_intro)
    return success_api_response({'list': restart_list})


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
    img = request.FILES.getlist('avatar')[0]
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
