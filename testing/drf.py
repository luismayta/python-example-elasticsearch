# -*- coding: utf-8 -*-
from rest_framework.test import (
    APIClient as APIClientDrf,
    APIRequestFactory as APIRequestFactoryDrf,
)
from testing.mixins import RequestFactoryMixin


class APIRequestFactory(RequestFactoryMixin, APIRequestFactoryDrf):
    pass


class APIClient(RequestFactoryMixin, APIClientDrf):
    pass
