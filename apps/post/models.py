# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class Post(TimeStampedModel):
    class Meta:
        db_table = "post"
        ordering = ["-created"]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.title
