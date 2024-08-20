from django.contrib import admin

from .models import Customer, Merchant, Order, OrderProduct, Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


class OrderProductInline(admin.TabularInline):
    model = OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "merchant", "order_date")
    inlines = (OrderProductInline,)
