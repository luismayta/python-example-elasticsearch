# -*- coding: utf-8 -*-
from blog import mixins
from enum import Enum, unique


@unique
class Administrator(mixins.ConvertEnumMixin, Enum):
    """Class for admin"""

    username = "gideon"
    email = "gideon_goddard@yopmail.com"
    first_name = "Gideon"
    last_name = "Goddard"
    phone_number = "+51959196850"


@unique
class Seller(mixins.ConvertEnumMixin, Enum):
    """Class user vars for test."""

    username = "elliot"
    email = "elliot@yopmail.com"
    first_name = "Elliot"
    last_name = "alderson"
    phone_number = "+51959196850"
