"""
关于餐馆和tag的api
    1. 创建tag（）
    2. 创建或附加tag
    3. 去除联系
    4. 获取所有tag
    5. 用tag筛选餐馆
"""
from django.http import HttpRequest
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .. import *
from ..models import Restaurant
from ..models import Tag
from src.application.users.api.auth import jwt_auth


@response_wrapper
@jwt_auth()
@require_POST
def create_tag(request: HttpRequest):
    target_id = request.POST.get('target_id')
    tag_name_list = request.POST.get('tags')
    target = Restaurant.objects.filter(id=target_id).first()
    creater = request.user
    if target is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅不存在！")
    if target.creater != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "无权限！")

    for tag_name in tag_name_list:
        tag = Tag(tag_name=tag_name, creater=creater)
        tag.save()
        target.tags.add(tag)

    return success_api_response({'message': '创建成功'})


@response_wrapper
@jwt_auth()
@require_POST
def refer_tag(request):
    target_id = request.POST.get('target_id')
    tag_name_list = request.POST.get('tags')
    target = Restaurant.objects.filter(id=target_id).first()
    creater = request.user
    if target is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅不存在！")
    if target.creater != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "无权限！")

    for tag_name in tag_name_list:
        tag = Tag.objects.filter(tag_name=tag_name).first()
        # 如果tag不存在，就创建一个
        if tag is None:
            tag = Tag(tag_name=tag_name, creater=creater)
            tag.save()
        target.tags.add(tag)

    return success_api_response({'message': '创建成功'})


@response_wrapper
@jwt_auth()
@require_http_methods(['DELETE'])
def delete_tag(request: HttpRequest):
    target_id = request.POST.get('target_id')
    tag_name = request.POST.get('tag')
    target = Restaurant.objects.filter(id=target_id).first()
    tag = Tag.objects.filter(tag_name=tag_name).first()
    if target is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅不存在！")
    if tag is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "标签不存在！")
    if target.creater != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "无权限！")

    target.tags.remove(tag)

    # 如果没有餐厅使用这个tag了，就删除这个tag
    if tag.restaurant_set.count() == 0:
        tag.delete()

    return success_api_response({'message': '删除成功'})


@response_wrapper
@jwt_auth()
@require_GET
def get_tag_list(request: HttpRequest):
    tag_list = Tag.objects.all()
    data = []
    for tag in tag_list:
        data.append({'name': tag.tag_name})
    return success_api_response({'list': data})


@response_wrapper
@jwt_auth()
@require_GET
def get_tag_restaurant_list(request: HttpRequest):
    tag_name = request.GET.get('tag')
    tag = Tag.objects.filter(tag_name=tag_name).first()
    if tag is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "标签不存在！")
    restaurant_list = tag.restaurant_set.all()
    data = []
    for restart in restaurant_list:
        restart_intro = {'id': restart.id,
                     'name': restart.name,
                     'img_url': restart.get_img_url(),
                     'phone': restart.phone,
                     'referer': restart.creater.name,
                     }
        tags_name = []
        for tag in restart.tags:
            tags_name.append(tag.tag_name)
        restart_intro.update({'tags': tags_name})
        data.append(restart_intro)
    return success_api_response({'list': data})

