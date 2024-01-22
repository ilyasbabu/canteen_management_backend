from django.db import models
from common.models import TimeStamp
from .student import Student


class Status(models.TextChoices):
    PLACED = "PLACED", "Order Placed"
    APPROVED = "APPROVED", "Order Approved"
    REJECTED = "REJECTED", "Order Rejected"
    READY = "READY", "Order Ready"
    DELIVERED = "DELIVERED", "Order Delivered"


class Order(TimeStamp):
    order_id = models.CharField(max_length=100, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=100, default=Status.PLACED, choices=Status.choices
    )
    remarks = models.TextField(null=True, blank=True)
    total_price = models.FloatField()
    total_quantity = models.IntegerField()

    def __str__(self):
        return self.order_id
