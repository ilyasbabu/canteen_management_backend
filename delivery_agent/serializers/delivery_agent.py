from rest_framework import serializers

class OrderListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    order_id = serializers.CharField(max_length=100)
    total_price = serializers.FloatField()
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()
