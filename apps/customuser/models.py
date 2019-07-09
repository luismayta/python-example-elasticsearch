# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from django.db import models
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models import signals


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, *args, **kwargs):
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not email:
            raise ValueError("Users must have an email")

        user = self.model(
            email=email, first_name=first_name.title(), last_name=last_name.title()
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name.title(),
            last_name=last_name.title(),
        )
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True

        user.save()
        return user

    def create_user_register(self, email, password, *args, **kwargs):

        if not email:
            raise ValueError("Users must have an email")

        user = self.model(email=email)
        user.is_superuser = False
        user.set_password(password)
        user.save()
        return user


class UserQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(is_active=True)


class User(AbstractUser, TimeStampedModel):
    class Meta:
        indexes = [models.Index(fields=["username", "email"])]
        db_table = "user"
        verbose_name_plural = "users"
        ordering = ["-created"]

    objects = UserManager.from_queryset(UserQuerySet)()

    # First Name and Last Name do not cover name patterns
    # around the globe.
    username = models.CharField(max_length=100)
    name = CharField(_("Name of User"), blank=True, max_length=255)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)

    # Personal Info.
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.username


@receiver(signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
