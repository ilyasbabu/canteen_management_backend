from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ValidationError
from accounts.services.authentication import CustomTokenAuthentication
from common.mixins import ExceptionHandlerMixin
from common.services import serialize_mobile_api, handle_error
from canteen_manager.services.food import get_food_list, create_food, get_food_category
from canteen_manager.serializers.food import FoodCreateSerializer


class FoodListAPI(ExceptionHandlerMixin, APIView):
    """API for listing food"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            data = get_food_list(user)
            res = serialize_mobile_api(True, data, "SUCCESS")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)


class FoodCategoryDropdownAPI(ExceptionHandlerMixin, APIView):
    """API for food category dropdown"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            data = get_food_category(user)
            res = serialize_mobile_api(True, data, "SUCCESS")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)



class FoodCreateAPI(ExceptionHandlerMixin, APIView):
    """API for adding food"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            serializer = FoodCreateSerializer(data=request.data)
            serializer.is_valid()
            if serializer.errors:
                error_list = [
                    f"{error.upper()}: {serializer.errors[error][0]}"
                    for error in serializer.errors
                ]
                print(error_list)
                raise ValidationError(error_list)
            create_food(user, **serializer.validated_data)
            res = serialize_mobile_api(True, msg="Food Created Successfully")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)
