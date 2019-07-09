# -*- coding: utf-8 -*-
import factory
from apps.comment.models import Comment
from apps.post.tests.factories import PostFactory


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment
        django_get_or_create = ("author",)

    post = factory.SubFactory(PostFactory)
    text = "text 1"
    author = "@slovacus"
