# -*- coding: utf-8 -*-
from rest_framework import status
from hamcrest import assert_that, equal_to
from django.urls import reverse


def test_list_user(django_db_setup, staff_client):
    """Validate filter for user."""
    url = reverse("user-list")
    response = staff_client.get(url)
    assert_that(response.status_code, equal_to(status.HTTP_200_OK))
