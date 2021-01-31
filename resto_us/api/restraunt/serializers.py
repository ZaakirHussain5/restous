from rest_framework import serializers
from .models import restraunt,restraunt_standards

class restrauntSerializer(serializers.ModelSerializer):
    class Meta:
        model = restraunt
        fields = '__all__'

class restraunt_standardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = restraunt_standards
        fields = '__all__'