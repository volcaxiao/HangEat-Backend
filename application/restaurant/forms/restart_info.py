from django.db.models import Avg
from ..models import Restaurant
from .. import *


def detail_info(request, restart: Restaurant)->dict:
    detail = model_to_dict(restart)
    detail['collectors_num'] = restart.collectors.count()
    detail['is_collected'] = request.user in restart.collectors.all()
    detail['avg_grade'] = restart.posts.aggregate(Avg('grade'))['grade__avg']
    detail['avg_price'] = restart.posts.aggregate(Avg('avg_price'))['avg_price__avg']
    return detail


def basic_info_list(request, restart_set: QuerySet, left: int, right: int)->dict:
    data = get_query_set_list(restart_set, left, right, ['id', 'name', 'img', 'creator', 'tags'])
    for item in data['list']:
        restaurant = Restaurant.objects.get(id=item['id'])
        item['collectors_num'] = restaurant.collectors.count()
        item['is_collected'] = request.user in restaurant.collectors.all()
        item['avg_grade'] = restaurant.posts.aggregate(Avg('grade'))['grade__avg']
        item['avg_price'] = restaurant.posts.aggregate(Avg('avg_price'))['avg_price__avg']
    return data