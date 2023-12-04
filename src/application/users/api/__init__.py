"""
在 init 中引入所有的 api 方法
"""

from .user_info import login_user
from .user_info import signup_user
from .user_info import logout_user
from .user_info import delete_user
from .user_info import update_user
from .user_info import update_avatar
from .user_info import change_password
from .user_info import forget_password
from .user_info import get_user_info

from .auth import refresh_token

from .email import send_captcha
from .email import change_email