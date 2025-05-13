import pytest
from src.main import Product

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
