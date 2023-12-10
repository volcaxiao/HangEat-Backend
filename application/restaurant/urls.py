from django.urls import path

from .api import *

urlpatterns = [
    path('create-resturant', creat_restaurant),
    path('get-restaurant-detail/<int:restart_id>', get_restaurant_detail),
    path('get-restaurant-num', get_restaurant_num),
    path('get-restaurant-list', get_restaurant_list),
    path('get-restarant-num-by-creater', get_restaurant_num_by_creater),
    path('get-restaurant-list-by-creater', get_restaurant_list_by_creater),
    path('edit-restaurant/<int:restart_id>', edit_restaurant),
    path('delete-restaurant/<int:restart_id>', delete_restaurant),

    # path('create-tag', create_tag),
    path('refer-tag', refer_tag),
    path('delete-tag', delete_tag),
    path('get-tag-num', get_tag_num),
    path('get-tag-list', get_tag_list),
    path('get-tag-resturant-num', get_restaurant_num_by_tag),
    path('get-tag-resturant-list', get_restaurant_list_by_tag),
]
