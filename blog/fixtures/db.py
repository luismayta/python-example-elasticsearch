# -*- coding: utf-8 -*-
import pytest
from django.core.management import call_command
from io import StringIO
from testing.validation import assert_test_database


@pytest.fixture
def django_db_setup(db, django_db_blocker):
    assert_test_database()
    new_io = StringIO()
    with django_db_blocker.unblock():
        call_command("migrate", stdout=new_io)
        call_command("create_permissions", stdout=new_io)
        call_command("populate", stdout=new_io)
        call_command(
            "createsuperuser",
            interactive=False,
            email="admin@yopmail.com",
            first_name="L",
            last_name="L",
            stdout=new_io,
        )
