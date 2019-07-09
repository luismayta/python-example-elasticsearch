# -*- coding: utf-8 -*-
from hamcrest import assert_that, instance_of, has_entries, equal_to
from blog.mixins import ConvertEnumMixin
from enum import Enum, unique


@unique
class TestEnum(ConvertEnumMixin, Enum):
    test = "value"


def test_mixins_instance():
    """Validate methods Mixin."""
    assert_that(TestEnum.to_dict(), instance_of(dict))
    assert_that(TestEnum.to_list(), instance_of(list))


def test_mixins_dict():
    """Validate dict of data Mixin."""
    dict_expected = {"test": "value"}
    assert_that(TestEnum.to_dict(), has_entries(dict_expected))


def test_mixins_list():
    """Validate list of data Mixin."""
    list_expected = ["value"]
    assert_that(TestEnum.to_list(), equal_to(list_expected))
