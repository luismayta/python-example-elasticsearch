# -*- coding: utf-8 -*-
from apps.customuser.models import User
from apps.customuser.tests.factories import UserFactory
from hamcrest import assert_that, instance_of


def test_make_user(django_db_setup):
    user = UserFactory()
    assert_that(user, instance_of(User))
