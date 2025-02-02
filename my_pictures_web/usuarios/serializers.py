from rest_framework import serializers
from .models import Pintor

class PintorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pintor
        fields = ['firstname', 'email', 'password']