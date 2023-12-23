"""
关于用户基本信息的API：
    1. 登录
    2. 注册
    3. 登出
    4. 删除用户
    5. 修改密码
    6. 修改邮箱
    7. 修改用户名
    8. 修改头像
    9. 获取用户信息
"""
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .. import *
from .auth import generate_token, generate_refresh_token, jwt_auth
from .email import varify_captcha
from ..models import User, AuthRecord

name_not_allow = ['default', 'delete']


@response_wrapper
@require_POST
def login_user(request: HttpRequest):
    post_data = parse_data(request)
    username = post_data.get('username')
    password = post_data.get('password')
    # 使用Django的authenticate函数验证用户名和密码
    user = authenticate(username=username, password=password)

    if user is None and '@' in username:
        # 使用邮箱登录
        tmp_user = User.objects.filter(email=username).first()
        if tmp_user is None:
            return failed_api_response(ErrorCode.CANNOT_LOGIN_ERROR, "用户名或邮箱不存在！")
        username = tmp_user.username
        user = authenticate(username=username, password=password)

    if user is not None and not user.isDelete:
        # 生成token
        token = generate_token(user)
        refresh_token = generate_refresh_token(user)
        if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        user.last_ip = ip
        return success_api_response({'message': '登录成功',
                                     'username': user.username,
                                     'token': token,
                                     'refresh_token': refresh_token})
    elif User.objects.filter(username=username).exists():
        # 密码错误
        return failed_api_response(ErrorCode.CANNOT_LOGIN_ERROR, "密码错误！")
    else:
        # 登录失败
        return failed_api_response(ErrorCode.CANNOT_LOGIN_ERROR, "用户名或邮箱不存在！")


@response_wrapper
@require_POST
def signup_user(request: HttpRequest):
    post_data = parse_data(request)
    username = post_data.get('username')
    password = post_data.get('password')
    email = post_data.get('email')
    captcha = post_data.get('captcha')

    # 检查是否有字段为空
    if username is None or password is None or email is None:
        return failed_api_response(ErrorCode.REQUIRED_ARG_IS_NULL_ERROR, '内容未填写完整')

    # 检查用户名是否已存在
    if User.objects.filter(username=username).exists():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '用户名已存在')
    if username in name_not_allow:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '非法取名')
    if User.objects.filter(email=email).exists():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "邮箱已注册")
    if password == '':
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "密码不能为空")
    if not varify_captcha(email, captcha):
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "验证码错误")
    if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 创建新用户
    User.objects.create_user(username=username, email=email, password=password, last_ip=ip)

    return success_api_response({'message': '注册成功'})


@response_wrapper
@jwt_auth()
@require_GET
def logout_user(request):
    # 登出用户
    AuthRecord.objects.filter(user=request.user).delete()
    return success_api_response({'message': '登出成功'})


@response_wrapper
@jwt_auth()
@require_http_methods(['DELETE'])
def delete_user(request: HttpRequest):
    # 获取用户
    user = request.user
    # 删除用户
    if user.avatar.name != 'avatar/default.jpg':
        user.avatar.delete()
    logout(request)
    user.username = "default"
    user.avatar.name = 'avatar/delete.png'
    user.motto = "该用户已注销"
    user.isDelete = True
    user.email.delete()
    user.save()
    AuthRecord.objects.filter(user=user).delete()
    return success_api_response({'message': '注销成功'})


@response_wrapper
@jwt_auth()
@require_POST
def change_password(request: HttpRequest):
    post_data = parse_data(request)
    old_password = post_data.get('old_password')
    new_password = post_data.get('new_password')

    # 使用Django的authenticate函数验证用户名和密码
    user = authenticate(username=request.user.username, password=old_password)
    if user is not None:
        # 修改密码
        user.password = make_password(new_password)
        user.save()
        return success_api_response({'message': '密码修改成功'})
    else:
        # 登录失败
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "原密码错误")


@response_wrapper
@require_POST
def forget_password(request: HttpRequest):
    post_data = parse_data(request)
    email = post_data.get('email')
    captcha = post_data.get('captcha')
    new_password = post_data.get('password')
    user = User.objects.filter(email=email).first()
    if user is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "邮箱未注册")
    if varify_captcha(email, captcha):
        user.password = make_password(new_password)
        user.save()
        return success_api_response({"message": "验证码正确，密码已修改"})
    else:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "验证码错误")


@response_wrapper
@jwt_auth()
@require_http_methods(['PUT'])
def update_user(request: HttpRequest):
    """
    更新用户信息:
        1. 更新用户名
        2. 更新个性签名
    """
    # 获取用户
    user = request.user
    # 获取数据
    put_data = parse_data(request)
    username = put_data.get('username')
    motto = put_data.get('motto')

    # 检查用户名是否已存在
    if username and User.objects.filter(username=username).exists():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '用户名已存在')
    elif username in name_not_allow:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '非法取名')
    elif username:
        user.username = username

    # 检查个性签名是否为空
    if motto:
        user.motto = motto

    # 更新用户
    user.save()
    return success_api_response({"message": "更新成功"})


@response_wrapper
@jwt_auth()
@require_POST
def update_avatar(request: HttpRequest):
    # 获取用户
    user = request.user
    # 获取数据
    avatar = request.FILES.getlist('avatar')[0] if len(request.FILES.getlist('avatar')) > 0 else None

    if avatar:
        if avatar.size > 1024 * 1024 * 2:
            return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片大小不能超过2MB")
        if user.avatar.name != 'avatar/default.png':
            user.avatar.delete()
        avatar.name = user.username + str(timezone.now()) + '.png'
        user.avatar = avatar
    else:
        return failed_api_response(ErrorCode.REQUIRED_ARG_IS_NULL_ERROR, "图片不能为空")

    # 更新用户
    user.save()
    return success_api_response({"message": "更新成功", "url": user.avatar.url})


@response_wrapper
@jwt_auth()
@require_GET
def get_user_info(request):
    user = request.user
    subscriptions_num = user.subscriptions.all().count()
    subscribers_num = user.subscribers.all().count()
    return success_api_response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "avatar": user.avatar.url,
        "motto": user.motto,
        "subscriptions_num": subscriptions_num,
        "subscribers_num": subscribers_num
    })


@response_wrapper
@require_GET
def get_user_info_by_id(request: HttpRequest, user_id: int):
    target_user = User.objects.filter(id=user_id).first()
    if target_user is None:
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "用户不存在！")
    subscriptions_num = target_user.subscriptions.all().count()
    subscribers_num = target_user.subscribers.all().count()
    return success_api_response({
        "id": target_user.id,
        "username": target_user.username,
        "email": target_user.email,
        "avatar": target_user.avatar.url,
        "motto": target_user.motto,
        "subscriptions_num": subscriptions_num,
        "subscribers_num": subscribers_num
    })
