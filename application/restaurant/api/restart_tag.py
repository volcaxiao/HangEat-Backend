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
from application.users.api.auth import jwt_auth


# @response_wrapper
# @jwt_auth()
# @require_POST
# def create_tag(request: HttpRequest):
#     target_id = request.POST.get('target_id')
#     tag_name_list = request.POST.get('tags')
#     target = Restaurant.objects.filter(id=target_id).first()
#     creater = request.user
#     if target is None:
#         return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅不存在！")
#     if target.creater != request.user:
#         return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "无权限！")
#
#     for tag_name in tag_name_list:
#         tag = Tag(name=tag_name, creater=creater)
#         tag.save()
#         target.tags.add(tag)
#
#     return success_api_response({'message': '创建成功'})


@response_wrapper
@jwt_auth()
@require_POST
def refer_tag(request):
    target_id = request.POST.get('target_id')
    tag_name_list = request.POST.getlist('tags')
    target = Restaurant.objects.filter(id=target_id).first()
    creater = request.user
    if target is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅不存在！")
    if target.creater != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "无权限！")

    for tag_name in tag_name_list:
        tag = Tag.objects.filter(name=tag_name).first()
        # 如果tag不存在，就创建一个
        if tag is None:
            tag = Tag(name=tag_name, creater=creater)
            tag.save()
        target.tags.add(tag)

    return success_api_response({'message': '创建成功'})


@response_wrapper
@jwt_auth()
@require_http_methods(['DELETE'])
def delete_tag(request: HttpRequest):
    target_id = request.GET.get('target_id')
    tag_name = request.GET.get('tag')
    target = Restaurant.objects.filter(id=target_id).first()
    tag = Tag.objects.filter(name=tag_name).first()
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
def get_tag_num(request: HttpRequest):
    tag_cnt = Tag.objects.count()
    return success_api_response({'tag_num': tag_cnt})


@response_wrapper
@jwt_auth()
@require_GET
def get_tag_list(request: HttpRequest):
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    data = get_query_set_list(Tag.objects, left, right, ['name'])
    return success_api_response(data)


@response_wrapper
@jwt_auth()
@require_GET
def get_restaurant_num_by_tag(request: HttpRequest):
    query_tags = request.GET.getlist('tags')
    tags = Tag.objects.filter(name__in=query_tags)
    restaurant_list = Restaurant.objects.filter(tags__in=tags).distinct()
    return success_api_response({'restaurant_num': restaurant_list.count()})


@response_wrapper
@jwt_auth()
@require_GET
def get_restaurant_list_by_tag(request: HttpRequest):
    query_tags = request.GET.getlist('tags')
    tags = Tag.objects.filter(name__in=query_tags)
    restaurant_list = Restaurant.objects.filter(tags__in=tags).distinct()
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    data = get_query_set_list(restaurant_list, left, right, ['id', 'name', 'img', 'creater', 'tags'])
    return success_api_response(data)

