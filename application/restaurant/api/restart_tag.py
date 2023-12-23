"""
关于餐馆和tag的api
    2. 创建或附加tag
    3. 去除联系
    4. 获取所有tag
    5. 用tag筛选餐馆
"""
from ..forms import *
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .. import *
from ..models import Restaurant
from ..models import Tag
from application.users.api.auth import jwt_auth


@response_wrapper
@jwt_auth()
@require_POST
def refer_tag(request):
    post_data = parse_data(request)
    target_id = post_data.get('target_id')
    tag_name_list = post_data.get('tags')
    target = Restaurant.objects.filter(id=target_id).first()
    creator = request.user
    if target is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅不存在！")
    if target.creator != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "无权限！")

    for tag_name in tag_name_list:
        tag = Tag.objects.filter(name=tag_name).first()
        # 如果tag不存在，就创建一个
        if tag is None:
            tag = Tag(name=tag_name, creator=creator)
            tag.save()
        target.tags.add(tag)

    return success_api_response({'message': '创建成功'})


@response_wrapper
@jwt_auth()
@require_http_methods(['DELETE'])
def delete_tag(request: HttpRequest):
    delete_data = parse_data(request)
    target_id = delete_data.get('target_id')
    tag_name = delete_data.get('tag_name')
    target = Restaurant.objects.filter(id=target_id).first()
    tag = Tag.objects.filter(name=tag_name).first()
    if target is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅不存在！")
    if tag is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "标签不存在！")
    if target.creator != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "无权限！")

    target.tags.remove(tag)

    # 如果没有餐厅使用这个tag了，就删除这个tag
    if tag.restaurants.count() == 0:
        tag.delete()

    return success_api_response({'message': '删除成功'})


@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_tag_num(request: HttpRequest):
    tag_cnt = Tag.objects.count()
    return success_api_response({'tag_num': tag_cnt})


@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_tag_list(request: HttpRequest):
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    data = get_query_set_list(Tag.objects, left, right, ['name'])
    for item in data['list']:
        refer_cnt = Tag.objects.get(name=item['name']).restaurants.count()
        if refer_cnt == 0:
            tag = Tag.objects.get(name=item['name'])
            tag.delete()
            data['list'].remove(item)
    return success_api_response(data)
