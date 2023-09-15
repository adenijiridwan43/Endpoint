from rest_framework import serializers
from .models import personBio

class personBioSerializer(serializers.ModelSerializer):
    class Meta:
        model = personBio
        fields = ('__all__')