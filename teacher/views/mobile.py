from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ValidationError
from accounts.services.authentication import CustomTokenAuthentication
from common.mixins import ExceptionHandlerMixin
from common.services import serialize_mobile_api, handle_error
from canteen_manager.services.food import (
    get_food_list_for_teacher,
    get_food_detail_for_teacher,
    approve_food,
)


class FoodListAPI(ExceptionHandlerMixin, APIView):
    """API for listing food"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            data = get_food_list_for_teacher(user)
            res = serialize_mobile_api(True, data, "SUCCESS")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)


class FoodDetailAPI(ExceptionHandlerMixin, APIView):
    """API for detail food"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            user = request.user
            data = get_food_detail_for_teacher(user, id)
            res = serialize_mobile_api(True, data, "SUCCESS")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)


class FoodApproveAPI(ExceptionHandlerMixin, APIView):
    """API for approve food"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            user = request.user
            approve_food(user, id)
            res = serialize_mobile_api(True,msg= "Food Approved Successfully")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)
