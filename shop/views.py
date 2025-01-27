from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from shop.models import Cart, CartItem


# Create your views here.


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

def basket_view(request):
    return render(request, 'shop/basket.html')





def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический логин после регистрации
            return redirect('index')  # Перенаправление на главную страницу
    else:
        form = UserCreationForm()
    return render(request, 'reg.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Перенаправление на главную страницу
    else:
        form = AuthenticationForm()
    return render(request, 'join.html', {'form': form})


@login_required
def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'basket.html', {'cart': cart})