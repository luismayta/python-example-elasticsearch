# -*- coding: utf-8 -*-
import pytest
from django.conf import settings
from django.test import RequestFactory
from testing.drf import APIClient
from blog.taskapp.celery import app
from apps.customuser.tests.factories import StaffFactory, UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()


@pytest.fixture(scope="module")
def celery_app(request):
    app.conf.update(CELERY_ALWAYS_EAGER=True)
    return app


@pytest.fixture
def anonymous_client():
    """Anonymous client for REST API."""
    client = APIClient()
    return client


@pytest.fixture
def api_client():
    """Anonymous client for REST API."""
    client = APIClient()
    user = UserFactory()
    client.credentials(HTTP_AUTHORIZATION="Token " + user.auth_token.key)
    return client


@pytest.fixture
def staff_client():
    """Staff client for REST API."""
    client = APIClient()
    user = StaffFactory()
    client.credentials(HTTP_AUTHORIZATION="Token " + user.auth_token.key)
    return client
