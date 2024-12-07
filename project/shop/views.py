from django.shortcuts import render
from django.shortcuts import redirect
from .models import Cart, CartItem, Product

def index(request):
    return render(request, 'shop/index.html')


def catalog(request):
    products = Product.objects.all()  # Получаем все продукты из базы данных
    return render(request, 'shop/catalog.html', {'products': products})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)  # Создаем корзину для пользователя, если её нет

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)  # Ищем, есть ли этот товар в корзине

    if not created:
        cart_item.quantity += 1  # Если товар уже есть в корзине, увеличиваем количество
        cart_item.save()

    return redirect('catalog')  # Перенаправляем на страницу каталога

def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shop/basket.html', {'cart_items': cart_items, 'total_price': total_price})


# Увеличение количества товара в корзине
def increase_quantity(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')  # Перенаправление на страницу корзины

# Уменьшение количества товара в корзине
def decrease_quantity(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  # Если количество товара 1, удаляем его из корзины
    return redirect('cart')
