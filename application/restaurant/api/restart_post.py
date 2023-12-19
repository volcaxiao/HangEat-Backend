"""
关于餐厅下的附议帖子及其回复的api
    1. 创建帖子
    2. 创建帖子下的评论
    3. 删除帖子
    4. 删除评论
    5. 帖子点赞
    6. 评论点赞
    7. 举报帖子
    8. 举报评论
"""
from django.http import HttpRequest
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .. import *
from ..models import Restaurant, Post, Comment
from application.users.api.auth import jwt_auth


@response_wrapper
@jwt_auth()
@require_POST
def creat_post(request):
    user = request.user
    post_data = parse_data(request)
    restart_id = post_data.get('restart_id')
    title = post_data.get('title')
    content = post_data.get('content')
    grade = post_data.get('grade')
    image = post_data.get('image')

    if Restaurant.objects.filter(id=restart_id).exists():
        restart = Restaurant.objects.get(id=restart_id)
        post = Post(title=title, content=content, creator=user, restart=restart, grade=grade)
        if image:
            post.image = image
        post.save()
        return success_api_response({"message": "创建成功！"})
    else:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅不存在！")


@response_wrapper
@jwt_auth()
@require_POST
def upload_image(request):
    user = request.user
    image = request.FILES.get('image')

    if image is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片为空！")
    if image.size > 1024 * 1024 * 2:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片大小超过2M！")
    if image.content_type not in ['image/jpeg', 'image/png']:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片格式不正确！")

    url = upload_img_file(image)
    if url is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片上传失败！")

    return success_api_response({"message": "上传成功！", "url": url})


@response_wrapper
@jwt_auth()
@require_POST
def creat_comment(request):
    user = request.user
    post_data = parse_data(request)
    post_id = post_data.get('post_id')
    reply_id = post_data.get('reply_id')
    content = post_data.get('content')
    post = Post.objects.get(id=post_id).first()
    if post:
        comment = Comment(content=content, refer_post=post, author=user)
        if reply_id:
            reply_to = Comment.objects.filter(id=reply_id).first()
            if not reply_to:
                return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "回复评论不存在！")
            comment.reply_to = reply_to
        comment.save()
        return success_api_response({"message": "创建成功！"})
    else:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "帖子不存在！")


@response_wrapper
@jwt_auth()
@require_GET
def get_restaurant_post(request: HttpRequest, restart_id: int):
    pass
