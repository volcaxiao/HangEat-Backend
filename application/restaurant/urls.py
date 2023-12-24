from django.urls import path

from .api import *

urlpatterns = [
    # 餐馆基本信息
    path('create-restaurant', creat_restaurant),
    path('update-restaurant/<int:restart_id>', update_restaurant),
    path('update-image/<int:restart_id>', update_image),
    path('get-restaurant-detail/<int:restart_id>', get_restaurant_detail),
    path('get-restaurant-num', get_restaurant_num),
    path('get-restaurant-list/<int:order_type>', get_restaurant_list),
    path('delete-restaurant/<int:restart_id>', delete_restaurant),
    path('get-recommend-list', get_recommend_list),
    # tag
    path('refer-tag', refer_tag),
    path('delete-tag', delete_tag),
    path('get-tag-num', get_tag_num),
    path('get-tag-list', get_tag_list),
    # post
    path('upload-image', upload_image),
    path('create-post', creat_post),
    path('update-post-image/<int:post_id>', update_post_image),
    path('get-post-num/<int:target_id>', get_post_num),
    path('get-post-list/<int:target_id>', get_post_list),
    path('get-post-num-by-user/<int:user_id>', get_post_num_by_user),
    path('get-post-list-by-user/<int:user_id>', get_post_list_by_user),
    path('get-post-detail/<int:post_id>', get_post_detail),
    path('agree-post/<int:post_id>', agree_post),
    path('disagree-post/<int:post_id>', disagree_post),
    path('delete-post/<int:post_id>', delete_post),
    path('update-post/<int:post_id>', update_post),
    path('get-hot-posts/<int:target_id>', get_hot_posts),
    # comment
    path('create-comment', creat_comment),
    path('get-comment-num/<int:post_id>', get_comment_num),
    path('get-comment-list/<int:post_id>', get_comment_list),
    path('agree-comment/<int:comment_id>', agree_comment),
    path('disagree-comment/<int:comment_id>', disagree_comment),
    path('delete-comment/<int:comment_id>', delete_comment),
    path('update-comment/<int:comment_id>', update_comment),
]
