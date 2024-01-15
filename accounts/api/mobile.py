import traceback
import sys

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ValidationError
from accounts.services.authentication import CustomTokenAuthentication
from accounts.services.mobile import user_login
from accounts.serializers.mobile import UserLoginSerializer, UserLoginResultSerializer
from common.mixins import ExceptionHandlerMixin
from common.services import serialize_mobile_api


class LoginAPI(ExceptionHandlerMixin,APIView):
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
            msg = "Something went wrong.Please contact the administrator."
            error_info = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(error_info)
            if isinstance(e, ValidationError):
                error_info = "\n".join(e.messages)
                msg = e.messages
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)

