#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

