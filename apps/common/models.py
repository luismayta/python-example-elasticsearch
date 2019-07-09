# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class CommonModel(TimeStampedModel):

    """
    Common abstract base class.
    """

    name = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
