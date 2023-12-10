from django.urls import path

from .api import *

urlpatterns = [
    path('create-resturant', creat_restaurant),
    path('get-resturant-detail/<int:restart_id>', get_restaurant_detail),
    path('get-resturant-num', get_restaurant_num),
    path('get-resturant-list', get_restaurant_list),
    path('edit-resturant/<int:restart_id>', edit_restaurant),
    path('delete-resturant/<int:restart_id>', delete_restaurant),

    # path('create-tag', create_tag),
    path('refer-tag', refer_tag),
    path('delete-tag', delete_tag),
    path('get-tag-num', get_tag_num),
    path('get-tag-list', get_tag_list),
    path('get-tag-resturant-num', get_restaurant_num_by_tag),
    path('get-tag-resturant-list', get_restaurant_list_by_tag),
]
