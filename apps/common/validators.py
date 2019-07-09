# -*- coding: utf-8 -*-
from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class GreaterThanValidator(validators.BaseValidator):
    message = "Ensure this value is greater than %(limit_value)s."
    code = "gt_value"

    def compare(self, a, b):
        return a <= b


@deconstructible
class LessThanValidator(validators.BaseValidator):
    message = "Ensure this value is less than %(limit_value)s."
    code = "lt_value"

    def compare(self, a, b):
        return a >= b
