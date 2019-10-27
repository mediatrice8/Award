# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Comments, Profile, Projects
from django.contrib import admin

# Register your models here.
admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Comments)