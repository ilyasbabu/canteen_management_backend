from rest_framework import serializers


class StudentCreateSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)


class OrderPlaceSerializer(serializers.Serializer):
    products = serializers.JSONField()
    delivery_time = serializers.CharField()


class OrderListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    order_id = serializers.CharField(max_length=100)
    total_price = serializers.FloatField()
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()


class OrderItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    food_id = serializers.CharField(max_length=100)
    food_name = serializers.SerializerMethodField()
    quantity = serializers.IntegerField()
    price = serializers.FloatField()
    image_url = serializers.SerializerMethodField()

    def get_food_name(self, obj):
        return obj.food.name

    def get_image_url(self, obj):
        return obj.food.image_url if obj.food.image_url else None


class OrderDetailSerializer(serializers.Serializer):
    order_id = serializers.CharField(max_length=100)
    total_price = serializers.FloatField()
    total_quantity = serializers.IntegerField()
    delivery_time = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    remarks = serializers.CharField(max_length=100)
    items = serializers.SerializerMethodField()

    def get_delivery_time(self, obj):
        return (
            obj.delivery_time.strftime("%d-%m-%Y %H:%M:%S")
            if obj.delivery_time
            else None
        )

    def get_status(self, obj):
        return obj.get_status_display()

    def get_items(self, obj):
        order_items = obj.items.filter(is_active=True)
        serializer = OrderItemSerializer(order_items, many=True)
        return serializer.data
