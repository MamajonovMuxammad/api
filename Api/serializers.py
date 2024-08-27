from rest_framework import serializers
from .models import *

class SubjectSerializer(serializers.ModelSerializer):
  class Meta:
      model = Cartochka
      fields = ['id', 'title', 'slug', 'description']