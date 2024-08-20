from rest_framework import serializers

from .models import Customer, Merchant, Order, OrderProduct, Product


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("name",)


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ("name",)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "price")


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = ("product", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    merchant = MerchantSerializer()
    products = OrderProductSerializer(source="orderproduct_set", many=True)

    class Meta:
        model = Order
        fields = ("customer", "merchant", "order_date", "products")
