# -*- coding: utf-8 -*-
from testing.drf import APIClient
from testing.mixins import TestCaseMixin


class TestCase(TestCaseMixin):
    client_class = APIClient
