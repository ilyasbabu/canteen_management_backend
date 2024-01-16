from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    """Serializer to get the inputs from login user"""

    username = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False)


class UserLoginResultSerializer(serializers.Serializer):
    """Serializer for the login success details"""

    auth_token = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    name = serializers.CharField()
    type = serializers.CharField()


class UserPasswordChangeSerializer(serializers.Serializer):
    """Serializer to get the inputs from change password"""

    new_password = serializers.CharField(required=True, allow_blank=False)
    confirm_password = serializers.CharField(required=True, allow_blank=False)
