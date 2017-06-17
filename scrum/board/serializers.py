"""
adding serializers
"""

from rest_framework import serializers

from .models import Sprint

class SprintSerializer(serializers.ModelSerializer):

	class Meta:
		model = Sprint
		fields = ('id', 'name', 'description', 'end',)

