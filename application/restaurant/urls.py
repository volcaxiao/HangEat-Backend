from django.urls import path

from .api import *

urlpatterns = [
    path('create-restaurant', creat_restaurant),
    path('update-restaurant/<int:restart_id>', update_restaurant),
    path('update-image/<int:restart_id>', update_image),
    path('get-restaurant-detail/<int:restart_id>', get_restaurant_detail),
    path('get-restaurant-num', get_restaurant_num),
    path('get-restaurant-list', get_restaurant_list),
    path('delete-restaurant/<int:restart_id>', delete_restaurant),

    path('refer-tag', refer_tag),
    path('delete-tag', delete_tag),
    path('get-tag-num', get_tag_num),
    path('get-tag-list', get_tag_list),
    path('get-tag-restaurant-num', get_restaurant_num_by_tag),
    path('get-tag-restaurant-list', get_restaurant_list_by_tag),
]
