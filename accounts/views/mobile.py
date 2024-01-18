from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ValidationError
from accounts.services.authentication import CustomTokenAuthentication
from accounts.services.mobile import user_login, user_logout
from accounts.serializers.mobile import (
    UserLoginSerializer,
    UserLoginResultSerializer,
    UserPasswordChangeSerializer,
)
from common.mixins import ExceptionHandlerMixin
from common.services import serialize_mobile_api, handle_error


class LoginAPI(ExceptionHandlerMixin, APIView):
    """API for user login from mobile app"""

    authentication_classes = [CustomTokenAuthentication]

    def post(self, request):
        try:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid()
            if serializer.errors:
                error_list = [
                    f"{error.upper()}: {serializer.errors[error][0]}"
                    for error in serializer.errors
                ]
                print(error_list)
                raise ValidationError(error_list)
            data = user_login(**serializer.validated_data)
            result_serializer = UserLoginResultSerializer(data)
            res = serialize_mobile_api(
                True, result_serializer.data, "Logged In Succesfully"
            )
            return Response(status=status.HTTP_201_CREATED, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)


class LogoutAPI(ExceptionHandlerMixin, APIView):
    """API for user logout from mobile app"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            user_logout(user)
            res = serialize_mobile_api(True, msg="Logged Out Succesfully")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)


class ChangePasswordAPI(ExceptionHandlerMixin, APIView):
    """API for user password change from mobile app"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            serializer = UserPasswordChangeSerializer(data=request.data)
            serializer.is_valid()
            if serializer.errors:
                error_list = [
                    f"{error.upper()}: {serializer.errors[error][0]}"
                    for error in serializer.errors
                ]
                print(error_list)
                raise ValidationError(error_list)
            password = serializer.validated_data["new_password"]
            confirm_password = serializer.validated_data["confirm_password"]
            if password != confirm_password:
                msg = "Both password and confirm password should be same!"
                res = serialize_mobile_api(False, msg, "ERROR")
                return Response(status=status.HTTP_404_NOT_FOUND, data=res)
            user.set_password(password)
            user.save()
            res = serialize_mobile_api(True, msg="Password changed successfully")
            return Response(status=status.HTTP_201_CREATED, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)
