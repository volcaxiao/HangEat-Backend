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
from django.http import HttpRequest
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .. import *
from .auth import generate_token, generate_refresh_token, jwt_auth
from .email import varify_captcha
from ..models import User


@response_wrapper
@require_POST
def login_user(request: HttpRequest):
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 使用Django的authenticate函数验证用户名和密码
    user = authenticate(username=username, password=password)

    if user is None and '@' in username:
        # 使用邮箱登录
        tmp_user = User.objects.filter(email=username).first()
        if tmp_user is None:
            return failed_api_response(ErrorCode.CANNOT_LOGIN_ERROR, "用户名或邮箱不存在！")
        username = tmp_user.username
        user = authenticate(username=username, password=password)

    if user is not None:
        # 登录成功
        login(request, user)
        # 生成token
        token = generate_token(user)
        refresh_token = generate_refresh_token(user)
        if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        user.last_ip = ip
        return success_api_response({'message': '登录成功',
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
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    captcha = request.POST.get('captcha')

    # 检查是否有字段为空
    if username is None or password is None or email is None:
        return failed_api_response(ErrorCode.REQUIRED_ARG_IS_NULL_ERROR, '内容未填写完整')

    # 检查用户名是否已存在
    if User.objects.filter(username=username).exists():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '用户名已存在')
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
    logout(request)

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
    user.delete()
    return success_api_response({'message': '注销成功'})


@response_wrapper
@jwt_auth()
@require_POST
def change_password(request: HttpRequest):
    old_password = request.POST.get('old_password')
    new_password = request.POST.get('new_password')

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
    email = request.POST.get('email')
    captcha = request.POST.get('captcha')
    new_password = request.POST.get('password')
    user = User.objects.filter(email=email).first()
    print(user, email, captcha, new_password)
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
    username = request.POST.get('username')
    motto = request.POST.get('motto')

    # 检查用户名是否已存在
    if username and User.objects.filter(username=username).exists():
        return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '用户名已存在')
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
@require_http_methods(['PUT'])
def update_avatar(request: HttpRequest):
    # 获取用户
    user = request.user
    # 获取数据
    avatar = request.FILES.getlist('avatar')[0]

    if avatar:
        if avatar.size > 1024 * 1024 * 2:
            return failed_api_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "图片大小不能超过2MB")
        if user.avatar.name != 'avatar/default.png':
            user.avatar.delete()
        avatar.name = user.username + '.png'
        user.avatar = avatar
    else:
        return failed_api_response(ErrorCode.REQUIRED_ARG_IS_NULL_ERROR, "图片不能为空")

    # 更新用户
    user.save()
    return success_api_response({"message": "更新成功", "url": user.get_avatar_url()})


@response_wrapper
@jwt_auth()
@require_GET
def get_user_info(request: HttpRequest):
    user = request.user
    return success_api_response({
        "username": user.username,
        "email": user.email,
        "avatar": user.get_avatar_url(),
        "motto": user.motto
    })
