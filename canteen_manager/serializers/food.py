from rest_framework import serializers


class FoodCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()
    category_id = serializers.CharField(max_length=100)
