from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "{}".format(self.name)


class Merchant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "{}".format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return "{}".format(self.name)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through="OrderProduct")

    def __str__(self) -> str:
        return "{}-{}-{}".format(self.customer, self.merchant, self.order_date)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return "{}-{}".format(self.product, self.quantity)
