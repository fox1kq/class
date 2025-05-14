import pytest
from src.main import Product, Category

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