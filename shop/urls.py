from django.urls import path  # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Добавление в корзину
    path('cart/', views.cart, name='cart'),
    path('basket.html', views.basket_view, name='basket'),  # Новый маршрут
    path('increase_quantity/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]

