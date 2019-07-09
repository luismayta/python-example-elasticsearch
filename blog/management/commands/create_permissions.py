# -*- coding: utf-8 -*-
from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    """
    Create get an patch missing permissions for every ContentType.
    """

    _message_finish = "Successfully create permissions"

    help = "Create get an patch missing permissions for every ContentType"

    def create_rest_permissions(self):
        Permission = apps.get_model("auth", "Permission")
        ContentType = apps.get_model("contenttypes", "ContentType")
        for content_type in ContentType.objects.all():
            name = content_type.name.lower()
            codename = "".join(name.split())
            # Get and patch are being added to make it RESTful.
            methods = ["get", "add", "change", "patch", "delete"]
            for method in methods:
                permission = Permission.objects.filter(
                    codename="{}_{}".format(method, codename), content_type=content_type
                )
                if permission.exists():
                    continue
                Permission.objects.create(
                    codename="{}_{}".format(method, codename),
                    name="Can {} {}".format(method, name),
                    content_type=content_type,
                )

    def handle(self, *args, **options):
        self.create_rest_permissions()
        self.stdout.write(self._message_finish)
