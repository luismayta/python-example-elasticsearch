# -*- coding: utf-8 -*-
class ConvertEnumMixin:
    @classmethod
    def to_list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def to_dict(cls):
        return {item.name: item.value for item in cls}
