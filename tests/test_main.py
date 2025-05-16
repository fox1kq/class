import pytest
from src.main import Product, Category, Smartphone, LawnGrass

@pytest.fixture
def smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                      "S23 Ultra", 256, "Серый")

@pytest.fixture
def smartphone2():
    return Smartphone("iPhone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


def test_price_setter_validation(monkeypatch):
    p = Product("Хлеб", "Белый хлеб", 40, 10)

    p.price = -10
    assert p.price == 40

    p.price = 0
    assert p.price == 40

    monkeypatch.setattr("builtins.input", lambda _: "n")
    p.price = 30
    assert p.price == 40

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


def test_add_product_correct_type(smartphone1):
    category = Category("Смартфоны", "Описание")
    category.add_product(smartphone1)
    assert len(category.products) == 1


def test_add_product_wrong_type():
    category = Category("Смартфоны", "Описание")
    with pytest.raises(TypeError):
        category.add_product("не продукт")


def test_sum_same_type(smartphone1, smartphone2):
    total = smartphone1 + smartphone2
    expected = smartphone1.price * smartphone1.quantity + smartphone2.price * smartphone2.quantity
    assert total == expected


def test_sum_different_type_raises(grass1, smartphone1):
    with pytest.raises(TypeError):
        smartphone1 + grass1
