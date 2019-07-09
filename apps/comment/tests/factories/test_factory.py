# -*- coding: utf-8 -*-
import pytest
from hamcrest import assert_that, instance_of
from . import CommentFactory
from apps.comment.models import Comment

test_instances = [(CommentFactory, Comment)]


@pytest.mark.parametrize("factory, class_name", test_instances)
def test_instance(factory, class_name, django_db_setup):
    instance = factory()
    assert_that(instance, instance_of(class_name))
