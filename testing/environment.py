# -*- coding: utf-8 -*-
from .cases import TestCase


def before_scenario(context, scenario):
    context.test_case = TestCase()
    context.test_case.setUpClass()


def after_scenario(context, scenario):
    context.test_case.tearDownClass()
    del context.test_case
