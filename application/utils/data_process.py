import json
import uuid
from itertools import chain

from django.core.files.storage import get_storage_class
from django.db import models
from django.db.models import QuerySet
from django.http import HttpRequest
from django.conf import settings

def parse_data(request: HttpRequest) -> dict:
    """Parse request body and generate python dict

    Args:
        request (HttpRequest): all http request

    Returns:
        | request body is malformed = None
        | otherwise                 = python dict
    """
    try:
        return json.loads(request.body.decode())
    except json.JSONDecodeError:
        return None


def get_query_set_num(query_set: QuerySet):
    """Get the number of query set

    Args:
        query_set (QuerySet): django query set

    Returns:
        int: number of query set
    """
    return query_set.all().count()


def get_query_set_list(query_set: QuerySet, left: int, right: int, fields: list = None, exclude: list = None):
    """Get the list of query set

    Args:
        exclude: list of exclude fields        : list of include fields
        query_set (QuerySet): django query set
        left (int): left index
        right (int): right index
    """
    query_set_num = get_query_set_num(query_set)
    query_set = query_set.all()
    left = max(0, min(left, right, query_set_num))
    right = min(query_set_num, max(left, right))
    query_set = query_set[left:right]
    data = {'all_num': query_set_num,
            'query_cnt': right - left}
    query_list = []
    for instance in query_set:
        ins_dict = model_to_dict(instance, fields, exclude)
        query_list.append(ins_dict)
    data.update({'list': query_list})
    return data


# ModelForms #################################################################
def model_to_dict(instance, fields=None, exclude=None):
    """
    Return a dict containing the data in ``instance`` suitable for passing as
    a Form's ``initial`` keyword argument.

    ``fields`` is an optional list of field names. If provided, return only the
    named.

    ``exclude`` is an optional list of field names. If provided, exclude the
    named from the returned dict, even if they are listed in the ``fields``
    argument.
    """
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
        if fields is not None and f.name not in fields:
            continue
        if exclude and f.name in exclude:
            continue
        if isinstance(f, models.ImageField) or isinstance(f, models.FileField):
            data[f.name] = f.value_from_object(instance).url
        elif isinstance(f, models.ManyToManyField):
            data[f.name] = [i.pk for i in f.value_from_object(instance)]
        else:
            data[f.name] = f.value_from_object(instance)
    return data


def upload_img_file(image):
    """
    ！ 上传单张图片
    :param image: b字节文件
    :return: 若成功返回图片路径，若不成功返回空
    """
    # 生成文件编号，如果文件名重复的话在oss中会覆盖之前的文件
    number = uuid.uuid4()
    # 生成文件名
    base_img_name = 'assert/' + str(number) + '.jpg'
    # 生成外网访问的文件路径
    image_name = settings.OSS_MEDIA_URL + base_img_name
    # 这个是阿里提供的SDK方法 bucket是调用的4.1中配置的变量名
    # res = bucket.put_object(base_img_name, image)
    storage = get_storage_class()()
    storage.save(base_img_name, image)
    return image_name
