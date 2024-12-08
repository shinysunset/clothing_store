#from django.db import models
#from django.contrib.auth.models import User

# class Product(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Название продукта")
#     description = models.TextField(verbose_name="Описание")
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
#     stock = models.PositiveIntegerField(verbose_name="Количество на складе")
#     image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение")
#
#     def str(self):
#         return self.name
#
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
#     products = models.ManyToManyField(Product, through='CartItem', verbose_name="Продукты")
#
#     def str(self):
#         return f"Корзина {self.user.username}"
#
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Корзина")
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
#     quantity = models.PositiveIntegerField(verbose_name="Количество")
#
#     def str(self):
#         return f'{self.product.name} - {self.quantity}'

# shop/models.py
# shop/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        # Убедитесь, что формат строки соответствует ожидаемому в тестах
        return f"{self.quantity} x {self.product.name}"
