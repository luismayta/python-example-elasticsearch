# -*- coding: utf-8 -*-
import json

from behave import then
from hamcrest import assert_that, not_none
from testing.tools import del_key_by_value, normalize_data


def factory_method_request(context, method, items, url, format_type=None):

    methods_available = {"get": request_method_get, "post": request_method_post}
    method_function = methods_available.get(method, None)
    if not method_function:
        raise ValueError("{} not available".format(method))

    url = "{}".format(url)
    return method_function(
        context=context, method=method, items=items, url=url, format_type=format_type
    )


def response_to_dict(response):
    data = {"content": None}
    if isinstance(response.content, bytes):
        content = response.content.decode("utf-8")

    try:
        data = json.loads(content)
    except json.decoder.JSONDecodeError:
        data["content"] = content

    data["status_code"] = response.status_code
    return normalize_data(data)


def request_method_get(context, method, items, url, format_type=None):
    response_list = list()
    for item in items:
        item = del_key_by_value(item)
        response = context.request.get(url, data=item)
        assert_that(response, not_none)
        response_list.append(response_to_dict(response))

    return response_list


def request_method_post(context, method, items, url, format_type=None):
    if format_type == "json":
        response = context.request.post(
            url, json.dumps(items), content_type="application/json"
        )
        assert_that(response, not_none)
        return response_to_dict(response)

    response_list = list()

    for item in items:
        item = del_key_by_value(item)
        response = context.request.post(url, data=item)
        assert_that(response, not_none)
        response_list.append(response_to_dict(response))

    return response_list


@then(u'"{method}" the "{var}" to the url "{url}" with format "{format_type}":')
def method_the_var_to_the_url_with_format(context, method, var, url, format_type):
    if hasattr(context, var):
        items = getattr(context, var)

    response_list = factory_method_request(
        context=context, method=method, items=items, url=url, format_type=format_type
    )

    context.response = dict()
    context.response[var] = response_list


@then(u'"{method}" the "{var}" to the url "{url}":')
def method_the_var_with_resource(context, method, var, url):
    items = list()
    response_list = list()
    if hasattr(context, var):
        items = getattr(context, var)

    if not isinstance(items, (list, tuple)):
        items = [items]

    response_list = factory_method_request(
        context=context, method=method, items=items, url=url
    )

    context.response = dict()
    context.response[var] = response_list
