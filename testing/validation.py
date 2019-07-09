# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.management.base import CommandError


def assert_test_database():
    """
    Raises a CommandError in the event that the database name does not contain
    any reference to testing.

    Also checks South settings to ensure migrations are not implemented.
    """

    if "test" not in settings.DATABASES["default"]["NAME"]:
        raise CommandError("You must run with a test database")
