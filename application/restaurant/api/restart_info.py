"""
关于餐厅信息的API
    1. 创建餐厅
    2. 获取餐厅信息
    3. 获取餐厅列表
    4. 修改餐厅信息
    5. 删除餐厅
"""
from enum import IntEnum

from django.db.models import Avg, Count, F
from django.utils import timezone
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .. import *
from ..models import Restaurant, Tag
from application.users.api.auth import jwt_auth
from ...users.models import User
from ..forms import *


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
    return success_api_response({"message": "创建成功！", "id": restart.id})


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
    if description is not None and len(description) <= 200:
        restart.description = description
    if detail_addr is not None:
        restart.detail_addr = detail_addr
    if phone is not None:
        restart.phone = phone
    restart.save()
    if len(description) > 200:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "描述过长，其余修改已保存")
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
        img.name = restart.name + str(timezone.now()) + '.png'
        restart.img = img
    restart.save()
    return success_api_response({"message": "修改成功！"})


@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_restaurant_detail(request: HttpRequest, restart_id: int):
    restart = Restaurant.objects.get(id=restart_id)
    if restart is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    detail = detail_info(request, restart)
    return success_api_response(detail)


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


class OrderType(IntEnum):
    collectors_num = 0
    avg_grade = 1
    avg_price = 2
    create_time = 3

def get_query_set_ordered(query_set: QuerySet, order_type: OrderType, reverse: bool=False):
    """
        reverse: 默认降序，设为True就是升序
    """
    if order_type == OrderType.collectors_num:
        if reverse:
            return query_set.annotate(collectors_num=Count('collectors')).order_by('-collectors_num').reverse()
        return query_set.annotate(collectors_num=Count('collectors')).order_by('-collectors_num')
    if order_type == OrderType.avg_grade:
        if reverse:
            return query_set.annotate(avg_grade=Avg('posts__grade')).order_by('-avg_grade').reverse()
        return query_set.annotate(avg_grade=Avg('posts__grade')).order_by('-avg_grade')
    if order_type == OrderType.avg_price:
        if reverse:
            return query_set.annotate(price_avg=Avg('posts__avg_price')).order_by('-price_avg').reverse()
        return query_set.annotate(price_avg=Avg('posts__avg_price')).order_by('-price_avg')
    if order_type == OrderType.create_time:
        if reverse:
            return  query_set.order_by('-created_at').reverse()
        return query_set.order_by('-created_at')

@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_restaurant_num(request: HttpRequest):
    creator_id = request.GET.get('creator_id')
    query_tags = request.GET.get('tags')
    restart_set = Restaurant.objects
    if creator_id is not None:
        restart_set = restart_set.filter(creator_id=creator_id)
    if query_tags is not None:
        query_tags = query_tags.split(',')
        restart_set = restart_set.filter(tags__name__contains=query_tags)
    return success_api_response({'restaurant_num': restart_set.count()})

@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_restaurant_list(request: HttpRequest, order_type: int):
    if order_type < 0 or order_type > 3:
        return failed_api_response(ErrorCode.NOT_FOUND_ERROR, "未知排序方式")
    order_type = OrderType(order_type)
    creator_id = request.GET.get('creator_id')
    query_tags = request.GET.get('tags')
    reverse = bool(int(request.GET.get("reverse")))
    left = int(request.GET.get("from"))
    right = int(request.GET.get("to"))
    restart_set = Restaurant.objects.all()
    if creator_id is not None:
        restart_set = restart_set.filter(creator_id=creator_id)
    if query_tags is not None:
        query_tags = query_tags.split(',')
        for tag in query_tags:
            restart_set &= Restaurant.objects.filter(tags__name=tag).all()
    data = basic_info_list(request, get_query_set_ordered(restart_set, order_type, reverse), left, right)
    return success_api_response(data)

# -------------------------------------------------------------------
# 推荐算法
# -------------------------------------------------------------------

def get_restart_associate(user: User)->dict:
    asso_dict = {}
    collect_restart = user.collections.all()
    for item in collect_restart:
        asso_dict.update({item: 2.+(asso_dict.get(item) if asso_dict.__contains__(item) else 0)})
    posts = user.posts.all()
    for item in posts:
        restart = item.restaurant
        asso_dict.update({restart: 0.3*item.grade+(asso_dict[restart] if asso_dict.__contains__(restart) else 0)})
    subscriptions = user.subscriptions.all()
    for subscription in subscriptions:
        for item in subscription.posts.all():
            restart = item.restaurant
            asso_dict.update({restart: 0.1*item.grade+(asso_dict[restart] if asso_dict.__contains__(restart) else 0)})
    agree_posts = user.agreedPosts.all()
    for item in agree_posts:
        restart = item.restaurant
        asso_dict.update({restart: 0.15*item.grade+(asso_dict[restart] if asso_dict.__contains__(restart) else 0)})
    return asso_dict

def get_restart_score(asso_dict: dict, best_price: float, restart: Restaurant):
    score = 0
    for tag in restart.tags.all():
        score += asso_dict[tag] if asso_dict.__contains__(tag) else 0
    avg_price = restart.posts.aggregate(Avg('avg_price'))['avg_price__avg']
    score += 10/(abs(avg_price-best_price)+1) if avg_price is not None and best_price is not None else 0
    return score

@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_recommend_list(request: HttpRequest):
    """
    推荐算法实现思路：
    tag的排序：
        用户收藏夹中的餐馆的tag的权重为2
        用户发帖的餐馆的tag权重为0.3*帖子评价的星级
        用户关注的用户的发帖的餐馆的tag权重为0.1*帖子评价的星级
        用户点赞的帖子的餐馆tag的权重为0.15*帖子评价的星级
    最终按照tag的权值给tag排序。
    价格的最优值：
        权重排布与上面一致。
    最终按照加权平均值取得最优价格。
    假如用户的相关数据过少，就采取随机的办法。
    """
    if request.user is None:
        data = basic_info_list(request, get_query_set_ordered(Restaurant.objects, OrderType.avg_grade), 0, 10)
        return success_api_response(data)
    # 计算权重值
    asso_dict = get_restart_associate(request.user)
    if len(asso_dict) == 0:
        data = basic_info_list(request, get_query_set_ordered(Restaurant.objects, OrderType.avg_grade), 0, 10)
        return success_api_response(data)
    asso_tag = {}
    total_price = 0
    total_wight = 0
    for restart, weight in asso_dict.items():
        the_price = restart.posts.aggregate(Avg('avg_price'))['avg_price__avg']
        if the_price:
            total_wight += weight
            total_price += the_price*weight
        for tag in restart.tags.all():
            asso_tag.update({tag: weight+(asso_tag[tag] if asso_tag.__contains__(tag) else 0)})
    best_price = total_price/total_wight if total_wight != 0 else None
    asso_tag = sorted(asso_tag.items(), key=lambda x: x[1], reverse=True)
    asso_tag = asso_tag[:10]
    asso_tag = dict(asso_tag)
    # 计算推荐值
    restart_list = {}
    for restart in Restaurant.objects.all():
        score = get_restart_score(asso_tag, best_price, restart)
        if score > 1: # 推荐值大才推荐
            restart_list.update({restart: score})
    if len(restart_list) < 2:
        data = basic_info_list(request, get_query_set_ordered(Restaurant.objects, OrderType.avg_grade), 0, 10)
        return success_api_response(data)
    restart_list = sorted(restart_list.items(), key=lambda x: x[1], reverse=True)
    restart_list = [item[0] for item in restart_list][:10]
    restart_list = Restaurant.objects.filter(pk__in=[x.pk for x in restart_list])
    data = basic_info_list(request, restart_list, 0, 10)
    return success_api_response(data)
