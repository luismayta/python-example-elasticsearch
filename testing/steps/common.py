# -*- coding: utf-8 -*-
import json

from behave import then, when
from hamcrest import assert_that, equal_to, not_none
from testing.tools import normalize_data


def factory_append(context, var):
    if len(context.table.rows) == 1:
        append_one(context, var)
    else:
        append_some(context, var)


def append_one(context, var):
    data = dict()
    for row in context.table:
        data = normalize_data(row.as_dict())
    setattr(context, var, data)


def append_some(context, var):
    data = list()
    for row in context.table:
        data.append(normalize_data(row.as_dict()))

    setattr(context, var, data)


@when(u'make "{var}" with')
def make_var_with(context, var):
    factory_append(context, var)

    variable = getattr(context, var)
    assert_that(variable, not_none())


@when(u'make "{var}" with "{field}"')
def make_var_with_field(context, var, field):
    data = dict()
    data_temp = dict()
    for row in context.table:
        data_temp = row.as_dict()

    for key, value in data_temp.items():
        data_temp[key] = json.loads(value)

    data = getattr(context, var)
    data[field] = data_temp

    setattr(context, var, data)

    variable = getattr(context, var)
    assert_that(variable, not_none())


@when(u'make "{var}" with some "{field}"')
def make_var_with_some_field(context, var, field):
    vars_convert_json = ("option", "prices")
    data = dict()
    data_list = list()

    for row in context.table:
        data = row.as_dict()
        for key in vars_convert_json:
            if data.get(key):
                data[key] = json.loads(data.get(key))
        data_list.append(data)

    data_var = getattr(context, var)
    data_var[field] = data_list
    setattr(context, var, data_var)


@then('the "{var}" with "{attribute}" must be "{value}"')
def and_the_var_with_attributes_mus_be_value(context, var, attribute, value):
    status_code = None
    if hasattr(context, var):
        response = getattr(context, var)
        if hasattr(response, attribute):
            status_code = getattr(response, attribute)

    assert_that(status_code, equal_to(value))
