# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ("id", "title", "author", "content", "created", "modified")
    list_filter = ("title",)
    search_fields = ("title",)
