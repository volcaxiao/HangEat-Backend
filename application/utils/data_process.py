import json
from itertools import chain
from django.http import HttpRequest


def parse_data(request: HttpRequest):
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


# # ModelForms #################################################################
#
# def model_to_dict(instance, fields=None, exclude=None):
#     """
#     Return a dict containing the data in ``instance`` suitable for passing as
#     a Form's ``initial`` keyword argument.
#
#     ``fields`` is an optional list of field names. If provided, return only the
#     named.
#
#     ``exclude`` is an optional list of field names. If provided, exclude the
#     named from the returned dict, even if they are listed in the ``fields``
#     argument.
#     """
#     opts = instance._meta
#     data = {}
#     for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
#         if not getattr(f, 'editable', False):
#             continue
#         if fields is not None and f.name not in fields:
#             continue
#         if exclude and f.name in exclude:
#             continue
#         data[f.name] = f.value_from_object(instance)
#     return data