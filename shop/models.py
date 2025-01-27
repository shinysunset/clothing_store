# from django.db import models
# from django.contrib.auth.models import User

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
from django.db import models  # type: ignore


# Модель для представления продукта

class Product(models.Model):
    # Название продукта (строка длиной до 100 символов)
    name = models.CharField(max_length=100)
    # Цена продукта (десятичное число с 2 знаками после запятой)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Описание продукта (текстовое поле)
    description = models.TextField()


    # Метод для строкового представления объекта (будет отображаться в админке и при выводе объектов)
    def __str__(self):
        return self.name


# Модель для представления корзины
class Cart(models.Model):
    # Связь с пользователем (каждая корзина привязана к одному пользователю)
    # "auth.User" - это стандартная модель пользователя в Django
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Дата и время создания корзины (заполняется автоматически)
    created_at = models.DateTimeField(auto_now_add=True)

    # Метод для строкового представления объекта корзины
    def __str__(self):
        return f"Cart for {self.user.username}"

# Модель для представления товара в корзине
class CartItem(models.Model):
    # Связь с корзиной (каждый товар привязан к одной корзине)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    # Связь с продуктом (каждый товар в корзине связан с конкретным продуктом)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    # Количество добавленных товаров в корзину
    quantity = models.PositiveIntegerField()

    # Метод для строкового представления объекта CartItem
    # Отображается количество и название продукта в корзине
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
