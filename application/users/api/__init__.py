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
from .user_info import get_user_info_by_id

from .auth import refresh_token

from .email import send_captcha
from .email import change_email

from .user_user import subscribe
from .user_user import unsubscribe
from .user_user import get_subscriptions_num
from .user_user import get_subscriptions_list
from .user_user import get_subscribers_num
from .user_user import get_subscribers_list
from .user_user import get_relation_between

from .user_restart import collect_restart
from .user_restart import uncollect_restart
from .user_restart import get_collections_num
from .user_restart import get_collections_list
