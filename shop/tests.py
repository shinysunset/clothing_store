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


class ProductModelTestCase(TestCase):
    def setUp(self):
        # Создаем пользователя для тестов
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Создаем продукт
        self.product = Product.objects.create(
            name='Test Product',
            price=99.99,
            description='A test product for testing purposes.'
        )

    def test_product_creation(self):
        # Проверяем, что продукт был создан
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 99.99)
        self.assertEqual(self.product.description, 'A test product for testing purposes.')

    def test_product_str_method(self):
        # Проверяем метод __str__ модели Product
        self.assertEqual(str(self.product), 'Test Product')


class CartModelTestCase(TestCase):
    def setUp(self):
        # Создаем пользователя для тестов
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Создаем корзину для пользователя
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_creation(self):
        # Проверяем, что корзина была создана
        self.assertEqual(self.cart.user.username, 'testuser')
        self.assertTrue(self.cart.created_at)

    def test_cart_str_method(self):
        # Проверяем метод __str__ модели Cart
        self.assertEqual(str(self.cart), 'Cart for testuser')


class CartItemModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', price=100)
        self.cart = Cart.objects.create(user=User.objects.create(username='testuser'))
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_cart_item_creation(self):
        # Проверяем, что элемент в корзине был создан
        self.assertEqual(self.cart_item.quantity, 2)
        self.assertEqual(self.cart_item.product.name, 'Test Product')
        self.assertEqual(self.cart_item.cart.user.username, 'testuser')


class ProductModelTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Test Product", price=100)

    def test_product_creation(self):
        """Проверяет, что продукт создается корректно"""
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 100)

    def test_product_str_method(self):
        """Проверяет строковое представление продукта"""
        product = Product.objects.get(name="Test Product")
        self.assertEqual(str(product), "Test Product")


class CartModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_creation(self):
        """Проверяет, что корзина создается корректно"""
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.user.username, "testuser")

    def test_cart_str_method(self):
        """Проверяет строковое представление корзины"""
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(str(cart), f"Cart for {self.user.username}")


class CartItemModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.product = Product.objects.create(name="Test Product", price=100)
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_cart_item_creation(self):
        """Проверяет создание элемента в корзине"""
        cart_item = CartItem.objects.get(cart=self.cart, product=self.product)
        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(cart_item.product.name, "Test Product")
        self.assertEqual(cart_item.cart.user.username, "testuser")

    def test_cart_item_str_method(self):
        """Проверяет строковое представление элемента в корзине"""
        cart_item = CartItem.objects.get(cart=self.cart, product=self.product)
        self.assertEqual(str(cart_item), "2 x Test Product")

