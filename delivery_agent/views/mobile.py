from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from accounts.services.authentication import CustomTokenAuthentication
from common.mixins import ExceptionHandlerMixin
from common.services import serialize_mobile_api, handle_error
from student.services.order import (
    get_order_list_for_agent,
    change_order_status_for_agent,
)
from student.models import Status
from delivery_agent.serializers.delivery_agent import OrderListSerializer


class OrderListAPI(ExceptionHandlerMixin, APIView):
    """API for listing ready to be picked orders"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            data = get_order_list_for_agent(user)
            serializer = OrderListSerializer(data, many=True)
            res = serialize_mobile_api(True, serializer.data, "SUCCESS")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)


class OrderStatusPickedAPI(ExceptionHandlerMixin, APIView):
    """API for changing status from READY to PICKED"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            user = request.user
            data = change_order_status_for_agent(user, id, Status.PICKED)
            res = serialize_mobile_api(True, data, "SUCCESS")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)


class OrderStatusDeliveredAPI(ExceptionHandlerMixin, APIView):
    """API for changing status from PICKED to DELIVERED"""

    authentication_classes = [CustomTokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            user = request.user
            data = change_order_status_for_agent(user, id, Status.DELIVERED)
            res = serialize_mobile_api(True, data, "SUCCESS")
            return Response(status=status.HTTP_200_OK, data=res)
        except Exception as e:
            msg = handle_error(e)
            res = serialize_mobile_api(False, msg, "ERROR")
            return Response(status=status.HTTP_404_NOT_FOUND, data=res)
