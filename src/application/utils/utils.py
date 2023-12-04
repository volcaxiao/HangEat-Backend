import warnings
from enum import unique, Enum

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@unique
class ErrorCode(Enum):
    """
    api error code enumeration
    """

    # success code family
    SUCCESS = 200  # deprecated
    SUCCESS_CODE = 200_00

    # bad request family
    INVALID_REQUEST_ARGS = 400  # deprecated
    BAD_REQUEST_ERROR = 400_00
    INVALID_REQUEST_ARGUMENT_ERROR = 400_01
    REQUIRED_ARG_IS_NULL_ERROR = 400_02
    STUDENT_CANNOT_LOGIN_ERROR = 400_03

    # unauthorized family
    UNAUTHORIZED = 401  # deprecated
    UNAUTHORIZED_ERROR = 401_00

    # refuse family
    REFUSE_ACCESS = 403  # deprecated
    REFUSE_ACCESS_ERROR = 403_00
    CONFIRM_CHECK_OUT = 403_01
    SEAT_ARRANGEMENT_ERROR = 403_02

    # not found family
    ITEM_NOT_FOUND = 404  # deprecated
    NOT_FOUND_ERROR = 404_00
    ACTIVE_EXAM_NOT_FOUND_ERROR = 404_01  # currently no active exam

    # duplicated family
    ITEM_ALREADY_EXISTS = 409  # deprecated
    DUPLICATED_ERROR = 409_00
