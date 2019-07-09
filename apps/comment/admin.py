# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ("id", "post", "text", "author", "created", "modified")
    list_filter = ("post", "author")
    search_fields = ("author", "post")
