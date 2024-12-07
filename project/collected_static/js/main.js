// Класс Item представляет отдельный товар в корзине
class Item {
  // Конструктор класса, инициализирует товар с id, ценой, количеством и категорией
  constructor(id, price, quantity = 1, category = '') {
    this.id = id; // Уникальный идентификатор товара
    this.price = price; // Цена товара
    this.quantity = quantity; // Количество товара
    this.category = category; // Категория товара (например, одежда, обувь и т. д.)
  }

  // Метод для расчета стоимости одного товара (цена * количество)
  calculateSum() {
    return this.price * this.quantity; // Возвращает стоимость товара
  }

  // Метод для увеличения количества товара на 1
  increaseQuantity() {
    this.quantity += 1; // Увеличиваем количество товара
  }

  // Метод для уменьшения количества товара на 1, но не ниже 1
  decreaseQuantity() {
    if (this.quantity > 1) {
      this.quantity -= 1; // Уменьшаем количество на 1, если оно больше 1
    }
  }
}

// Класс Basket представляет корзину покупок
class Basket {
  // Конструктор класса инициализирует корзину пустым массивом товаров
  constructor() {
    this.items = []; // Массив для хранения товаров в корзине
  }

  // Метод для расчета суммы товара в корзине на основе количества и цены
  calculateSum(numberInput, numberPrice, numberSum) {
    let currentCount = parseInt(numberInput.value); // Получаем количество товара
    let price = parseInt(numberPrice.textContent.trim()); // Получаем цену товара

    // Если количество товара некорректное или меньше 1, ставим сумму = 0
    if (isNaN(currentCount) || currentCount <= 0) {
      numberSum.textContent = "0"; // Отображаем 0 в случае ошибки
    } else {
      numberSum.textContent = currentCount * price; // Рассчитываем сумму товара
    }
  }

  // Метод для увеличения количества товара на 1 и пересчета суммы
  handlePlus(numberInput, numberPrice, numberSum) {
    let currentValue = parseInt(numberInput.value); // Получаем текущее количество товара
    numberInput.value = isNaN(currentValue) ? 1 : currentValue + 4; // Увеличиваем количество на 1
    this.calculateSum(numberInput, numberPrice, numberSum); // Пересчитываем сумму
  }

  // Метод для уменьшения количества товара на 1 и пересчета суммы
  handleMinus(numberInput, numberPrice, numberSum) {
    let currentValue = parseInt(numberInput.value); // Получаем текущее количество товара
    if (currentValue > 1) {
      numberInput.value = currentValue - 1; // Уменьшаем количество на 1
      this.calculateSum(numberInput, numberPrice, numberSum); // Пересчитываем сумму
    } else {
      numberInput.value = "1"; // Минимальное количество товара не может быть меньше 1
    }
  }

  // Метод для обновления общей стоимости всех товаров в корзине
  updateTotal(basketTovarBlocks) {
    let totalSum = 0; // Переменная для хранения общей суммы
    basketTovarBlocks.forEach(block => {
      let sumElement = block.querySelector("#summa"); // Находим элемент с суммой товара
      totalSum += parseFloat(sumElement.textContent) || 0; // Суммируем все суммы товаров
    });
    console.log(`Общая сумма: ${totalSum}`); // Логируем общую сумму товаров в корзине
  }

  // Метод для очистки корзины (удаляет все товары из корзины)
  clearBasket(basketTovarBlocks) {
    basketTovarBlocks.forEach(block => block.remove()); // Удаляем все товары из корзины
  }

  // Метод для проверки, пуста ли корзина
  checkBasketEmpty(basketTovarBlocks) {
    return basketTovarBlocks.length === 0; // Возвращаем true, если корзина пуста
  }

  // Метод для получения общего количества товаров в корзине
  getTotalItemCount(basketTovarBlocks) {
    let totalCount = 0; // Переменная для хранения общего количества товаров
    basketTovarBlocks.forEach(block => {
      let countElement = block.querySelector("#schit"); // Находим элемент с количеством товара
      totalCount += parseInt(countElement.value, 10) || 0; // Суммируем все количества товаров
    });
    return totalCount; // Возвращаем общее количество товаров
  }

  // Метод для получения самого дорогого товара из корзины
  getMostExpensiveItem(basketTovarBlocks) {
    let maxPrice = 0; // Переменная для хранения максимальной цены
    let mostExpensiveItem = null; // Переменная для хранения самого дорогого товара
    basketTovarBlocks.forEach(block => {
      let priceElement = block.querySelector("#price"); // Находим элемент с ценой товара
      let price = parseInt(priceElement.textContent.trim()); // Получаем цену товара
      if (price > maxPrice) {
        maxPrice = price; // Обновляем максимальную цену
        mostExpensiveItem = block; // Обновляем самый дорогой товар
      }
    });
    return mostExpensiveItem; // Возвращаем самый дорогой товар
  }

  // Метод для сортировки товаров по цене от дешевого к дорогому
  sortItemsByPrice(basketTovarBlocks) {
    return Array.from(basketTovarBlocks).sort((a, b) => {
      let priceA = parseInt(a.querySelector("#price").textContent.trim()); // Получаем цену первого товара
      let priceB = parseInt(b.querySelector("#price").textContent.trim()); // Получаем цену второго товара
      return priceA - priceB; // Сортируем товары по цене
    });
  }

  // Метод для фильтрации товаров по категории
  filterItemsByCategory(basketTovarBlocks, category) {
    return Array.from(basketTovarBlocks).filter(block => {
      let categoryElement = block.dataset.category; // Получаем категорию товара
      return categoryElement === category; // Фильтруем товары по категории
    });
  }
}

// Класс Discount предназначен для работы со скидками
class Discount {
  // Метод для применения скидки на общую сумму
  applyDiscount(totalSum, discountPercentage) {
    if (discountPercentage < 0 || discountPercentage > 100) {
      throw new Error("Некорректный процент скидки"); // Проверяем на корректность скидки
    }
    return totalSum - (totalSum * (discountPercentage / 100)); // Применяем скидку и возвращаем итоговую сумму
  }
}

// Класс Stock предназначен для работы со складом товаров
class Stock {
  constructor() {
    this.stock = {}; // Это объект, где ключами будут служить идентификаторы товаров, а значениями — количество этих товаров на складе.
  }

  // Метод для обновления складских остатков
  updateStock(stock, itemId, quantityChange) {
    if (!(itemId in stock)) {
      throw new Error("Товар не найден на складе"); // Проверяем, существует ли товар на складе
    }

    if (stock[itemId] <= 0) {
      throw new Error("Недостаточно товара на складе"); // Проверяем, есть ли товар на складе
    }

    stock[itemId] -= quantityChange; // Уменьшаем количество товара на складе

    if (stock[itemId] < 0) {
      throw new Error("Недостаточно товара на складе"); // Если товара не хватает, выбрасываем ошибку
    }

    return stock[itemId]; // Возвращаем обновленный остаток товара
  }

  // Метод для добавления товара на склад
  addItem(itemId, quantity) {
    if (this.stock[itemId]) {
      this.stock[itemId] += quantity; // Если товар уже есть на складе, увеличиваем его количество
    } else {
      this.stock[itemId] = quantity; // Если товара нет на складе, добавляем его
    }
  }
}

// Экспортируем классы для использования в других частях приложения или для тестирования
module.exports = { 
  Item,
  Basket,
  Discount,
  Stock 
};
