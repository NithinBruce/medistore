from rest_framework import serializers
from cure.models import Medicine

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'