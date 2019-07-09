# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel
from apps.post.models import Post


class Comment(TimeStampedModel):
    """Comment for Post

    """

    class Meta:
        db_table = "comment"
        ordering = ["-created"]

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.text
