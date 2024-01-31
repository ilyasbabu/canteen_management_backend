from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ValidationError
from accounts.services.authentication import CustomTokenAuthentication
from common.mixins import ExceptionHandlerMixin
from common.services import serialize_mobile_api, handle_error
from canteen_manager.services.food import get_food_list_for_student
from student.services.student import create_student, get_department_dropdown
from student.services.order import place_order, get_order_list_for_student, get_order_detail_for_student
from student.serializers.student import (
    StudentCreateSerializer,
    OrderPlaceSerializer,
    OrderListSerializer,
    OrderDetailSerializer,
)


class DepartmentDropdownAPI(ExceptionHandlerMixin, APIView):
    """API for department dropdown"""

    def get(self, request):
        try:
            data = get_department_dropdown()
            res = serialize_mobile_api(True, data, "SUCCESS")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)


class StudentCreateAPI(ExceptionHandlerMixin, APIView):
    """API for creating student"""

    authentication_classes = [CustomTokenAuthentication]

    def post(self, request):
        try:
            serializer = StudentCreateSerializer(data=request.data)
            serializer.is_valid()
            if serializer.errors:
                error_list = [
                    f"{error.upper()}: {serializer.errors[error][0]}"
                    for error in serializer.errors
                ]
                print(error_list)
                raise ValidationError(error_list)
            create_student(**serializer.validated_data)
            res = serialize_mobile_api(True, msg="Registered Successfully!")
            return Response(status=status.HTTP_201_CREATED, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)


class FoodListAPI(ExceptionHandlerMixin, APIView):
    """API for listing food"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            data = get_food_list_for_student(user)
            res = serialize_mobile_api(True, data, "SUCCESS")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)


class FoodOrderAPI(ExceptionHandlerMixin, APIView):
    """API for ordering food"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            serializer = OrderPlaceSerializer(data=request.data)
            serializer.is_valid()
            if serializer.errors:
                error_list = [
                    f"{error.upper()}: {serializer.errors[error][0]}"
                    for error in serializer.errors
                ]
                print(error_list)
                raise ValidationError(error_list)
            data = place_order(user, **serializer.validated_data)
            res = serialize_mobile_api(True, data, "Order Placed Succesfully")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)


class OrderListAPI(ExceptionHandlerMixin, APIView):
    """API for listing orders"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            data = get_order_list_for_student(user)
            serializer = OrderListSerializer(data, many=True)
            res = serialize_mobile_api(True, serializer.data, "SUCCESS")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)


class OrderDetailAPI(ExceptionHandlerMixin, APIView):
    """API for order detail"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            user = request.user
            data = get_order_detail_for_student(user, id)
            serializer = OrderDetailSerializer(data)
            res = serialize_mobile_api(True, serializer.data, "SUCCESS")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)