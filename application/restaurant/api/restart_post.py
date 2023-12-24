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


from django.db.models import Count
from django.utils import timezone
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
    restart_id = post_data.get('restaurant_id')
    title = post_data.get('title')
    content = post_data.get('content')
    if len(content) > 2000:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "帖子内容过长！")
    grade = post_data.get('grade')
    if grade not in [0, 1, 2, 3, 4, 5]:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "评分不合法！")
    price = post_data.get('price')
    if price < 0 or price > 9999:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "人均价格不合理！")

    if Restaurant.objects.filter(id=restart_id).exists():
        restart = Restaurant.objects.get(id=restart_id)
        post = Post(title=title, content=content, creator=user, restaurant=restart, grade=grade, avg_price=price)
        post.save()
        return success_api_response({"message": "创建成功！", "id": post.id})
    else:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅不存在！")

@response_wrapper
@jwt_auth()
@require_POST
def update_post_image(request: HttpRequest, post_id: int):
    post = Post.objects.get(id=post_id)
    if post is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '帖子不存在')
    if post.creator != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '无权修改')
    image = request.FILES.get('image') if request.FILES.get('image') else None
    if image is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片为空！")
    if image.size > 1024 * 1024 * 2:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片大小超过2M！")
    image.name = str(post_id) + str(timezone.now()) + '.png'
    post.image = image
    post.save()
    return success_api_response({"message": "修改成功！", "url": post.image.url})

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
    url = upload_img_file(image)
    if url is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片上传失败！")

    return success_api_response({"message": "上传成功！", "url": url})

@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_post_num(request: HttpRequest, target_id: int):
    post_num = Post.objects.filter(restaurant_id=target_id).count()
    return success_api_response({'post_num': post_num})

@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_post_list(request: HttpRequest, target_id: int):
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    post_list = Post.objects.filter(restaurant_id=target_id)
    data = get_query_set_list(post_list, left, right, ['id', 'title', 'content', 'grade', 'avg_price', 'creator', 'image', 'agrees'])
    for post in data['list']:
        post['agrees'] = len(post['agrees'])
        post['is_agreed'] = request.user in Post.objects.get(id=post['id']).agrees.all()
    return success_api_response(data)

@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_post_num_by_user(request: HttpRequest, user_id: int):
    post_num = Post.objects.filter(creator_id=user_id).count()
    return success_api_response({'post_num': post_num})


@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_post_list_by_user(request: HttpRequest, user_id: int):
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    post_list = Post.objects.filter(creator_id=user_id)
    data = get_query_set_list(post_list, left, right, ['id', 'title', 'content', 'grade', 'avg_price', 'creator', 'image', 'agrees'])
    for post in data['list']:
        post['agrees'] = len(post['agrees'])
        post['is_agreed'] = request.user in Post.objects.get(id=post['id']).agrees.all()
    return success_api_response(data)

@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_post_detail(request: HttpRequest, post_id: int):
    post = Post.objects.get(id=post_id)
    if post is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '帖子不存在')
    detail = model_to_dict(post)
    detail['agrees'] = post.agrees.count()
    detail['is_agreed'] = request.user in post.agrees.all()
    return success_api_response(detail)

@response_wrapper
@jwt_auth()
@require_POST
def agree_post(request: HttpRequest, post_id: int):
    post = Post.objects.get(id=post_id)
    user = request.user
    if post is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "帖子不存在")
    if user in post.agrees.all():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "已经点过赞了哦！")
    post.agrees.add(user)
    return success_api_response({"message": "点赞成功！"})

@response_wrapper
@jwt_auth()
@require_POST
def disagree_post(request: HttpRequest, post_id: int):
    post = Post.objects.get(id=post_id)
    user = request.user
    if post is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "帖子不存在")
    if user not in post.agrees.all():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "不可重复取消！")
    post.agrees.remove(user)
    return success_api_response({"message": "取消点赞成功！"})

@response_wrapper
@jwt_auth()
@require_http_methods(['DELETE'])
def delete_post(request: HttpRequest, post_id: int):
    post = Post.objects.get(id=post_id)
    if post is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '帖子不存在')
    if post.creator != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '无权删除')
    post.delete()
    return success_api_response({"message": "删除成功！"})

@response_wrapper
@jwt_auth()
@require_http_methods(['PUT'])
def update_post(request: HttpRequest, post_id: int):
    post = Post.objects.get(id=post_id)
    if post is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '帖子不存在')
    if post.creator != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '无权修改')
    post_data = parse_data(request)
    title = post_data.get('title')
    content = post_data.get('content')
    grade = post_data.get('grade')
    price = post_data.get('price')
    if title and len(title) < 50:
        post.title = title
    if content and len(content) < 2000:
        post.content = content
    if grade and grade in [0, 1, 2, 3, 4, 5]:
        post.grade = grade
    if price and 0 <= price <= 9999:
        post.avg_price = price
    post.save()
    return success_api_response({"message": "修改成功！"})

# -----------------------------------------------------
# 评论相关
# -----------------------------------------------------

@response_wrapper
@jwt_auth()
@require_POST
def creat_comment(request):
    user = request.user
    post_data = parse_data(request)
    post_id = post_data.get('post_id')
    reply_id = post_data.get('reply_id')
    content = post_data.get('content')
    post = Post.objects.get(id=post_id)
    if post:
        comment = Comment(content=content, refer_post=post, author=user)
        if reply_id:
            reply_to = Comment.objects.filter(id=reply_id).first()
            if not reply_to:
                return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "回复评论不存在！")
            comment.reply_to = reply_to
        comment.save()
        return success_api_response({"message": "创建成功！", "id": comment.id})
    else:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "帖子不存在！")

@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_comment_num(request: HttpRequest, post_id: int):
    comment_num = Comment.objects.filter(refer_post_id=post_id, reply_to__isnull=True).count()
    return success_api_response({'comment_num': comment_num})

def get_comment_info_below(comment: Comment, request: HttpRequest):
    comment_list = []
    for reply in comment.replies.all():
        comment_list.append(model_to_dict(reply, ['id', 'content', 'author', 'reply_to', 'agrees']))
        comment_list[-1]['agrees'] = len(comment_list[-1]['agrees'])
        comment_list[-1]['is_agreed'] = request.user in reply.agrees.all()
        comment_list += get_comment_info_below(reply, request)
    return comment_list

@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_comment_list(request: HttpRequest, post_id: int):
    left = int(request.GET.get('from'))
    right = int(request.GET.get('to'))
    comment_list = Comment.objects.filter(refer_post_id=post_id, reply_to__isnull=True)
    data = get_query_set_list(comment_list, left, right, ['id', 'content', 'author', 'reply_to', 'agrees'])
    for comment in data['list']:
        comment['agrees'] = len(comment['agrees'])
        comment_model = Comment.objects.get(id=comment['id'])
        comment['is_agreed'] = request.user in comment_model.agrees.all()
        replies = get_comment_info_below(comment_model, request)
        comment['replies'] = replies
    return success_api_response(data)

@response_wrapper
@jwt_auth()
@require_POST
def agree_comment(request: HttpRequest, comment_id: int):
    comment = Comment.objects.get(id=comment_id)
    user = request.user
    if comment is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "评论不存在")
    if user in comment.agrees.all():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "已经点过赞了哦！")
    comment.agrees.add(user)
    return success_api_response({"message": "点赞成功！"})

@response_wrapper
@jwt_auth()
@require_POST
def disagree_comment(request: HttpRequest, comment_id: int):
    comment = Comment.objects.get(id=comment_id)
    user = request.user
    if comment is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "评论不存在")
    if user not in comment.agrees.all():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "不可重复取消！")
    comment.agrees.remove(user)
    return success_api_response({"message": "取消点赞成功！"})

@response_wrapper
@jwt_auth()
@require_http_methods(['DELETE'])
def delete_comment(request: HttpRequest, comment_id: int):
    comment = Comment.objects.get(id=comment_id)
    if comment is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '评论不存在')
    if comment.author != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '无权删除')
    comment.delete()
    return success_api_response({"message": "删除成功！"})

@response_wrapper
@jwt_auth()
@require_http_methods(['PUT'])
def update_comment(request: HttpRequest, comment_id: int):
    comment = Comment.objects.get(id=comment_id)
    if comment is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '评论不存在')
    if comment.author != request.user:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '无权修改')
    post_data = parse_data(request)
    content = post_data.get('content')
    if content:
        comment.content = content
    comment.save()
    return success_api_response({"message": "修改成功！"})

@response_wrapper
@jwt_auth(allow_anonymous=True)
@require_GET
def get_hot_posts(request: HttpRequest, target_id: int):
    post_list = Post.objects.filter(restaurant_id=target_id).annotate(agree_num=Count('agrees')).order_by('-agree_num')
    data = get_query_set_list(post_list, 0, 5, ['id', 'title', 'grade', 'avg_price', 'creator', 'image', 'agrees'])
    for post in data['list']:
        post['agrees'] = len(post['agrees'])
        post['is_agreed'] = request.user in Post.objects.get(id=post['id']).agrees.all()
    return success_api_response(data)
