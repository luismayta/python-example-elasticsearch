# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from factory import DjangoModelFactory, Faker, PostGenerationMethodCall
from django.contrib.auth.models import Group


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ["username", "email"]

    username = Faker("user_name")
    password = PostGenerationMethodCall("set_password", "1234abcd")
    email = Faker("email")
    name = Faker("name")
    is_superuser = False
    is_active = True


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group
        django_get_or_create = ["name"]

    name = "administrator"


class StaffFactory(UserFactory):
    is_superuser = True
    is_staff = True
    is_active = True
    is_admin = True
