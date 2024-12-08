#from django.test import TestCase
#from django.contrib.auth.models import User
#from .models import Product, Cart, CartItem
#
# class ProductModelTestCase(TestCase):
#     def setUp(self):
#         self.product = Product.objects.create(
#             name="Laptop",
#             description="High performance laptop",
#             price=1000.00,
#             stock=10
#         )
#
#     def test_str_representation(self):
#         self.assertEqual(str(self.product), "Laptop")
#
#     def test_is_in_stock(self):
#         self.assertTrue(self.product.is_in_stock())
#         self.product.stock = 0
#         self.product.save()
#         self.assertFalse(self.product.is_in_stock())
#
# class CartModelTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="testuser", password="testpass")
#         self.product1 = Product.objects.create(
#             name="Laptop",
#             description="High performance laptop",
#             price=1000.00,
#             stock=10
#         )
#         self.product2 = Product.objects.create(
#             name="Mouse",
#             description="Wireless mouse",
#             price=50.00,
#             stock=20
#         )
#         self.cart = Cart.objects.create(user=self.user)
#         CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
#         CartItem.objects.create(cart=self.cart, product=self.product2, quantity=3)
#
#     def test_str_representation(self):
#         self.assertEqual(str(self.cart), f"Корзина {self.user.username}")
#
#     def test_total_price(self):
#         self.assertEqual(self.cart.total_price(), 1000 * 2 + 50 * 3)
#
# class CartItemModelTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="testuser", password="testpass")
#         self.product = Product.objects.create(
#             name="Laptop",
#             description="High performance laptop",
#             price=1000.00,
#             stock=10
#         )
#         self.cart = Cart.objects.create(user=self.user)
#         self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)
#
#     def test_str_representation(self):
#         self.assertEqual(str(self.cart_item), "Laptop - 2")
#
#     def test_total_item_price(self):
#         self.assertEqual(self.cart_item.total_item_price(), 2000.00)
# shop/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Cart, CartItem


# Тесты для модели Product
class ProductModelTestCase(TestCase):

    def setUp(self):
        """
        Метод setUp выполняется перед каждым тестом.
        Здесь мы создаем пользователя и продукт, которые будут использоваться в тестах.
        """
        self.product = Product.objects.create(name="Test Product", price=100)

    def test_product_creation(self):
        """
        Тестирует создание продукта.
        Проверяет, что продукт был правильно создан с нужными аттрибутами.
        """
        # Получаем продукт из базы данных
        product = Product.objects.get(name="Test Product")
        # Проверяем, что название и цена продукта соответствуют ожиданиям
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 100)

    def test_product_str_method(self):
        """
        Тестирует метод __str__ модели Product.
        Проверяет, что строковое представление продукта возвращает его название.
        """
        product = Product.objects.get(name="Test Product")
        self.assertEqual(str(product), "Test Product")


# Тесты для модели Cart
class CartModelTestCase(TestCase):

    def setUp(self):
        """
        Метод setUp выполняется перед каждым тестом.
        Здесь создаем пользователя и корзину для тестов.
        """
        self.user = User.objects.create(username="testuser")
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_creation(self):
        """
        Тестирует создание корзины.
        Проверяет, что корзина была правильно создана для пользователя.
        """
        # Получаем корзину из базы данных по пользователю
        cart = Cart.objects.get(user=self.user)
        # Проверяем, что корзина привязана к нужному пользователю
        self.assertEqual(cart.user.username, "testuser")

    def test_cart_str_method(self):
        """
        Тестирует метод __str__ модели Cart.
        Проверяет, что строковое представление корзины возвращает правильную строку.
        """
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(str(cart), f"Cart for {self.user.username}")


# Тесты для модели CartItem
class CartItemModelTestCase(TestCase):

    def setUp(self):
        """
        Метод setUp выполняется перед каждым тестом.
        Здесь создаем пользователя, продукт, корзину и элемент корзины для тестов.
        """
        self.user = User.objects.create(username="testuser")
        self.product = Product.objects.create(name="Test Product", price=100)
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_cart_item_creation(self):
        """
        Тестирует создание элемента в корзине.
        Проверяет, что элемент корзины был создан правильно и привязан к нужным объектам.
        """
        # Получаем элемент корзины
        cart_item = CartItem.objects.get(cart=self.cart, product=self.product)
        # Проверяем, что количество товара в корзине соответствует ожиданиям
        self.assertEqual(cart_item.quantity, 2)
        # Проверяем, что продукт и корзина правильно связаны
        self.assertEqual(cart_item.product.name, "Test Product")
        self.assertEqual(cart_item.cart.user.username, "testuser")

    def test_cart_item_str_method(self):
        """
        Тестирует метод __str__ модели CartItem.
        Проверяет, что строковое представление элемента корзины правильно отображает количество и название продукта.
        """
        cart_item = CartItem.objects.get(cart=self.cart, product=self.product)
        self.assertEqual(str(cart_item), "2 x Test Product")

