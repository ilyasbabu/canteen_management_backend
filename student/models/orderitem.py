from django.db import models
from common.models import TimeStamp
from .order import Order
from canteen_manager.models import Food


class OrderItem(TimeStamp):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
