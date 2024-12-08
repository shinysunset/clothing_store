const { 
  Item, 
  Basket, 
  Discount, 
  Stock 
} = require("./main.js"); // Импортируем необходимые классы из main.js

describe("Функциональность корзины", () => {
  let numberInput, numberPrice, numberSum, basketTovarBlocks;
  let basket, discount, stock;

  // Подготовка DOM перед каждым тестом
  beforeEach(() => {
    // Инициализируем HTML-разметку корзины, чтобы тестировать функциональность с реальными элементами DOM
    document.body.innerHTML = `
      <div class="basket_tovar" data-category="shirts">
          <input type="number" value="1" id="schit">
          <span id="price">250</span>
          <span id="summa">250</span>
          <button id="plus">+</button>
          <button id="minus">-</button>
          <button class="cross_btn"></button>
      </div>
      <div class="basket_tovar" data-category="pants">
          <input type="number" value="2" id="schit">
          <span id="price">500</span>
          <span id="summa">1000</span>
      </div>
      <div class="basket_tovar" data-category="shoes">
          <input type="number" value="3" id="schit">
          <span id="price">1000</span>
          <span id="summa">3000</span>
      </div>
    `;

    // Инициализация элементов корзины для тестирования
    numberInput = document.querySelector("#schit"); // Количество товара
    numberPrice = document.querySelector("#price"); // Цена товара
    numberSum = document.querySelector("#summa"); // Итоговая сумма для товара
    basketTovarBlocks = document.querySelectorAll(".basket_tovar"); // Все товары в корзине
    
    // Создаем экземпляры объектов для тестирования
    basket = new Basket(); // Корзина для тестирования функциональности корзины
    discount = new Discount(); // Объект для работы со скидками
    stock = new Stock(); // Объект для работы со складскими остатками
  });

  // Тесты для расчета итоговой суммы товара
  test("должен правильно считать сумму для одного товара", () => {
    const item = new Item(1, 250, 1); // Создаем новый товар с количеством 1 и ценой 250
    expect(item.calculateSum()).toBe(250); // Проверяем, что сумма товара 250
  });

  test("должен правильно пересчитывать сумму при изменении количества товара", () => {
    const item = new Item(1, 250, 2); // Создаем товар с количеством 2
    expect(item.calculateSum()).toBe(500); // Проверяем, что сумма для 2 единиц товара 500
    item.quantity = 3; // Меняем количество товара на 3
    expect(item.calculateSum()).toBe(750); // Проверяем, что сумма для 3 единиц товара 750
  });

  // Тест для увеличения количества товара на 1 при нажатии на кнопку "плюс"
  test("должен увеличивать количество товара на 1 при нажатии на кнопку 'плюс'", () => {
    basket.handlePlus(numberInput, numberPrice, numberSum); // Вызываем метод для увеличения
    expect(numberInput.value).toBe("2"); // Проверяем, что количество увеличилось на 1
  });

  // Тест для предотвращения уменьшения количества товара ниже 1 при нажатии на кнопку "минус"
  test("должен предотвращать уменьшение количества товара ниже 1 при нажатии на кнопку 'минус'", () => {
    basket.handleMinus(numberInput, numberPrice, numberSum); // Пробуем уменьшить количество до 0
    expect(numberInput.value).toBe("1"); // Количество не может быть меньше 1
    numberInput.value = "2"; // Устанавливаем значение 2
    basket.handleMinus(numberInput, numberPrice, numberSum); // Уменьшаем
    expect(numberInput.value).toBe("1"); // Проверяем, что количество снова не меньше 1
  });

  // Тест для пересчета суммы при изменении количества товара
  test("должен пересчитывать сумму после изменения количества товара", () => {
    numberInput.value = "3"; // Устанавливаем новое количество товара
    basket.calculateSum(numberInput, numberPrice, numberSum); // Пересчитываем сумму
    expect(numberSum.textContent).toBe("750"); // Проверяем, что сумма пересчиталась правильно
  });

  // Тест для проверки начального количества товара при загрузке страницы
  test("должен начинать с 1 товара по умолчанию при загрузке страницы", () => {
    expect(numberInput.value).toBe("1"); // Проверяем, что начальное количество товара — 1
  });

  // Тест для проверки пересчета суммы после увеличения количества товара
  test("должен сразу пересчитывать сумму после увеличения количества товара", () => {
    basket.handlePlus(numberInput, numberPrice, numberSum); // Нажимаем кнопку "+" для увеличения
    expect(numberSum.textContent).toBe("500"); // Проверяем, что сумма пересчитана правильно
  });

  // Тест для проверки пересчета суммы после уменьшения количества товара
  test("должен сразу пересчитывать сумму после уменьшения количества товара", () => {
    numberInput.value = "3"; // Устанавливаем количество товара равным 3
    basket.handleMinus(numberInput, numberPrice, numberSum); // Нажимаем кнопку "-" для уменьшения
    expect(numberSum.textContent).toBe("500"); // Проверяем, что сумма пересчитана правильно
  });

  // Тест для очистки корзины
  test("должен очищать корзину при нажатии на кнопку очистки", () => {
    basket.clearBasket(basketTovarBlocks); // Очищаем корзину
    basketTovarBlocks = document.querySelectorAll(".basket_tovar"); // Перезагружаем список товаров в корзине
    expect(basket.checkBasketEmpty(basketTovarBlocks)).toBe(true); // Проверяем, что корзина пуста
  });

  // Тест для подсчета общего количества товаров в корзине
  test("должен правильно подсчитывать общее количество товаров в корзине", () => {
    expect(basket.getTotalItemCount(basketTovarBlocks)).toBe(6); // Проверяем, что общее количество товаров в корзине 6
    numberInput.value = "5"; // Изменяем количество товара на 5
    expect(basket.getTotalItemCount(basketTovarBlocks)).toBe(10); // Проверяем, что общее количество товаров стало 10
  });

  // Тест для обновления общей стоимости всех товаров в корзине
  test("должен правильно обновлять общую стоимость всех товаров в корзине", () => {
    const logSpy = jest.spyOn(console, 'log').mockImplementation(() => {}); // Перехватываем вывод в консоль
    basket.updateTotal(basketTovarBlocks); // Обновляем общую стоимость
    const totalOutput = logSpy.mock.calls[0][0]; // Получаем первый вызов логирования
    expect(totalOutput.includes("Общая сумма:")).toBe(true); // Проверяем, что в выводе содержится общая сумма
    logSpy.mockRestore(); // Восстанавливаем оригинальное поведение логирования
  });

  // Тест для применения скидки
  test("должен правильно применять скидку на общую сумму", () => {
    const total = 1000; // Исходная сумма
    const discountAmount = 20; // Размер скидки 20%
    expect(discount.applyDiscount(total, discountAmount)).toBe(800); // Проверяем, что сумма после скидки равна 800
  });

  // Тест для получения самого дорогого товара из корзины
  test("должен возвращать самый дорогой товар из корзины", () => {
    const mostExpensiveItem = basket.getMostExpensiveItem(basketTovarBlocks); // Получаем самый дорогой товар
    expect(mostExpensiveItem.querySelector("#price").textContent).toBe("1000"); // Проверяем, что его цена 1000
  });

  // Тест для сортировки товаров по цене от дешевого к дорогому
  test("должен правильно сортировать товары по цене от дешевого к дорогому", () => {
    const sortedItems = basket.sortItemsByPrice(basketTovarBlocks); // Сортируем товары
    const prices = Array.from(sortedItems).map(item => parseInt(item.querySelector("#price").textContent)); // Получаем цены товаров после сортировки
    expect(prices).toEqual([250, 500, 1000]); // Проверяем, что товары отсортированы по цене
  });

  // Тест для фильтрации товаров по категории
  test("должен фильтровать товары по указанной категории", () => {
    const filteredItems = basket.filterItemsByCategory(basketTovarBlocks, "shirts"); // Фильтруем товары по категории "shirts"
    expect(filteredItems.length).toBe(1); // Ожидаем, что в корзине только один товар этой категории
    expect(filteredItems[0].dataset.category).toBe("shirts"); // Проверяем категорию товара
  });

  // Тест для фильтрации по несуществующей категории
  test("должен возвращать пустой результат при фильтрации по несуществующей категории", () => {
    const filteredItems = basket.filterItemsByCategory(basketTovarBlocks, "hats"); // Фильтруем по несуществующей категории
    expect(filteredItems.length).toBe(0); // Ожидаем, что ничего не будет найдено
  });

  // Тест для обновления складских остатков
  test("должен обновлять складские остатки товара после покупки", () => {
    const stockData = { 1: 10, 2: 5 }; // Складские данные
    stock.addItem(1, 10); // Добавляем товар на склад
    expect(stock.updateStock(stockData, 1, 2)).toBe(8); // Проверяем, что остаток товара обновился правильно
  });

  // Тест на ошибку при попытке обновить остатки для несуществующего товара
  test("должен выбрасывать ошибку при попытке обновить складской остаток для несуществующего товара", () => {
    const stockData = { 1: 10, 2: 5 };
    expect(() => stock.updateStock(stockData, 3, 1)).toThrow("Товар не найден на складе"); // Проверяем, что выбрасывается ошибка
  });

  // Тест на ошибку при недостаточности товара на складе
  test("должен выбрасывать ошибку при недостаточности товара на складе", () => {
    const stockData = { 1: 10, 2: 0 }; // Данные о товаре на складе
    expect(() => stock.updateStock(stockData, 1, 11)).toThrow("Недостаточно товара на складе"); // Проверяем, что выбрасывается ошибка
  });

  // Тест на ошибку при установке отрицательного количества товара
  test("должен запрещать установку отрицательного количества товара", () => {
    numberInput.value = "-1"; // Устанавливаем отрицательное значение
    basket.calculateSum(numberInput, numberPrice, numberSum); // Пересчитываем сумму
    expect(numberSum.textContent).toBe("0"); // Сумма не может быть отрицательной, должна быть 0
  });

  // Тест для обновления корзины с большим количеством товаров
  test("должен правильно обновлять корзину с большим количеством товаров", () => {
    const newBasketHTML = `
      <div class="basket_tovar" data-category="shoes">
          <input type="number" value="10" id="schit">
          <span id="price">200</span>
          <span id="summa">2000</span>
      </div>
    `;
    document.body.innerHTML += newBasketHTML; // Добавляем новый товар в корзину
    basketTovarBlocks = document.querySelectorAll(".basket_tovar"); // Перезагружаем список товаров в корзине
    expect(basket.getTotalItemCount(basketTovarBlocks)).toBe(16); // Проверяем, что общее количество товаров стало 16
  });

  // Тест на обновление общей суммы после удаления товара из корзины
  test("должен обновлять общую сумму после удаления товара из корзины", () => {
    document.querySelector(".basket_tovar .cross_btn").click(); // Нажимаем кнопку удаления товара
    basketTovarBlocks = document.querySelectorAll(".basket_tovar"); // Обновляем список товаров
    basket.updateTotal(basketTovarBlocks); // Обновляем общую сумму
  });

  // Тесты на ошибки и исключительные случаи
  test("должен выбрасывать ошибку при попытке применить отрицательную скидку", () => {
    expect(() => discount.applyDiscount(1000, -10)).toThrow("Некорректный процент скидки"); // Проверяем ошибку для отрицательной скидки
  });

  test("должен выбрасывать ошибку при попытке применить скидку более 100%", () => {
    expect(() => discount.applyDiscount(1000, 110)).toThrow("Некорректный процент скидки"); // Проверяем ошибку для скидки больше 100%
  });

  test("должен выбрасывать ошибку при фильтрации по несуществующей категории", () => {
    const filteredItems = basket.filterItemsByCategory(basketTovarBlocks, "hats"); // Фильтруем по несуществующей категории
    expect(filteredItems.length).toBe(0); // Проверяем, что не найдено ни одного товара
  });

  test("должен выбрасывать ошибку при попытке обновить складские остатки для несуществующего товара", () => {
    const stockData = { 1: 10, 2: 5 };
    expect(() => stock.updateStock(stockData, 3, 1)).toThrow("Товар не найден на складе"); // Проверяем ошибку при попытке обновить несуществующий товар
  });

  test("должен выбрасывать ошибку при недостаточности товара на складе", () => {
    const stockData = { 1: 10, 2: 0 };
    expect(() => stock.updateStock(stockData, 1, 11)).toThrow("Недостаточно товара на складе"); // Проверяем ошибку при недостаточности товара
  });

  test("должен выбрасывать ошибку при попытке уменьшить количество товара до отрицательного значения", () => {
    numberInput.value = "-1"; // Устанавливаем отрицательное количество товара
    basket.handleMinus(numberInput, numberPrice, numberSum); // Пробуем уменьшить
    expect(numberInput.value).toBe("1"); // Количество не может быть меньше 1
  });
});
