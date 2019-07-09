# -*- coding: utf-8 -*-
import factory
from apps.post.models import Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
        django_get_or_create = ("author",)

    title = "elasticsearch"
    author = "@slovacus"
    content = "this is content"
