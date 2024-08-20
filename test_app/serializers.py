from rest_framework import serializers

from .models import Customer, Merchant, Order, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ("product", "quantity")


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("name",)


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ("name",)


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(source="orderproduct_set", many=True)
    customer = CustomerSerializer()
    merchant = MerchantSerializer()

    class Meta:
        model = Order
        fields = ("customer", "merchant", "order_date", "products")
