# -*- coding: utf-8 -*-
from PIL import Image
from hamcrest import assert_that, instance_of
import tempfile
from apps.common.resize import ResizeToCircle


def test_resize_circle(django_db_setup, media_storage):
    image = Image.new("L", (100, 100))
    image = ResizeToCircle(100).process(image)
    tmp_file = tempfile.NamedTemporaryFile(suffix=".png")
    image.save(tmp_file)
    assert_that(image.size, instance_of(tuple))
