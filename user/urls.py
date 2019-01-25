#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path,include
from user import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/v1.0/user/', views.user_list),
]
urlpatterns = format_suffix_patterns(urlpatterns)