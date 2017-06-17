# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import authentication, permissions
from rest_framework import viewsets

from .models import Sprint
from .serializers import SprintSerializer

# Create your views here.

class DefaultMixin(object):
	"""
	Default settings for view authentication, permissions,
	filtering and pagination.
	"""

	authentication_class = (
		authentication.BasicAuthentication,
		authentication.TokenAuthentication,
	)

	permission_classes = (
		permissions.IsAuthenticated,
	)

	paginate_by = 25
	paginate_by_param = 'page_size'
	max_paginate_by = 100

class SprintViewSet(viewsets.ModelViewSet):
	"""
	API endpoint for listing and creating sprints.
	"""

	queryset = Sprint.objects.order_by('end')
	serializer_class = SprintSerializer


