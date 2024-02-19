from rest_framework import serializers


class OrderListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    order_id = serializers.CharField(max_length=100)
    total_price = serializers.FloatField()
    status = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()
    student_department = serializers.SerializerMethodField()
    student_mobile = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()

    def get_student_name(self, obj):
        return obj.student.user.name

    def get_student_department(self, obj):
        return obj.student.get_department_display()

    def get_student_mobile(self, obj):
        return obj.student.user.mobile
