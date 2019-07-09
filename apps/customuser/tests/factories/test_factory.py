# -*- coding: utf-8 -*-
from . import UserFactory
from apps.customuser.models import User
from hamcrest import assert_that, instance_of


def test_make_user(django_db_setup):
    user = UserFactory()
    assert_that(user, instance_of(User))
