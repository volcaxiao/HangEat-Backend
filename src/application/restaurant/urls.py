from django.urls import path

from .api import *

urlpatterns = [
    path('create-resturant', creat_restaurant),
    path('get-resturant-detail/<int:restart_id>', get_restaurant_detail),
    path('get-resturant-list', get_restaurant_list),
    path('edit-resturant/<int:restart_id>', edit_restaurant),
    path('delete-resturant/<int:restart_id>', delete_restaurant),

    path('create-tag', create_tag),
    path('refer-tag', refer_tag),
    path('delete-tag', delete_tag),
    path('get-tag-list', get_tag_list),
    path('get-tag-resturant-list', get_tag_restaurant_list),
]
