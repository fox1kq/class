import pytest
from src.main import Product, Category, Smartphone, LawnGrass

def test_price_setter_validation(monkeypatch):
    p = Product("Хлеб", "Белый хлеб", 40, 10)

    # Попытка установить цену < 0
    p.price = -10
    assert p.price == 40

    # Попытка установить цену = 0
    p.price = 0
    assert p.price == 40

    # Попытка понизить цену, пользователь отвечает "n"
    monkeypatch.setattr("builtins.input", lambda _: "n")
    p.price = 30
    assert p.price == 40

    # Попытка понизить цену, пользователь отвечает "y"
    monkeypatch.setattr("builtins.input", lambda _: "y")
    p.price = 30
    assert p.price == 30


def test_product_str():
    product = Product("Test", "desc", 100, 3)
    assert str(product) == "Test, 100 руб. Остаток: 3 шт."

def test_category_str():
    p1 = Product("Test1", "desc", 50, 2)
    p2 = Product("Test2", "desc", 100, 5)
    cat = Category("Тестовая", "тест", [p1, p2])
    assert str(cat) == "Тестовая, количество продуктов: 7 шт."

def test_product_add():
    p1 = Product("Test1", "desc", 10, 5)
    p2 = Product("Test2", "desc", 20, 3)
    assert p1 + p2 == (10 * 5 + 20 * 3)

    def setUp(self):
        self.smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                                      "S23 Ultra", 256, "Серый")
        self.smartphone2 = Smartphone("iPhone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
        self.grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        self.grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    def test_add_product_correct_type(self):
        category = Category("Смартфоны", "Описание")
        category.add_product(self.smartphone1)
        self.assertEqual(len(category.products), 1)

    def test_add_product_wrong_type(self):
        category = Category("Смартфоны", "Описание")
        with self.assertRaises(TypeError):
            category.add_product("не продукт")

    def test_sum_same_type(self):
        total = self.smartphone1 + self.smartphone2
        expected = (self.smartphone1.price * self.smartphone1.quantity +
                    self.smartphone2.price * self.smartphone2.quantity)
        self.assertEqual(total, expected)