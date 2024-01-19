from rest_framework import serializers


class StudentCreateSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)
