# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin  # noqa F401
from .models import Sprint, Task

# Register your models here.
admin.site.register(Sprint)
admin.site.register(Task)
