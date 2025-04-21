import pytest



@pytest.fixture
def products():
    return [
        Product("iPhone 15", "512GB, Gray", 210000.0, 8),
        Product("Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5),
        Product("Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]

@pytest.fixture
def category(products):
    # Сброс счётчиков перед тестом
    Category.category_count = 0
    Category.product_count = 0

    return Category("Смартфоны", "Умные телефоны нового поколения", products)

def test_product_init(products):
    product = products[0]
    assert product.name == "iPhone 15"
    assert product.description == "512GB, Gray"
    assert product.price == 210000.0
    assert product.quantity == 8

def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == "Умные телефоны нового поколения"
    assert len(category.products) == 3

def test_category_counts(category):
    assert Category.category_count == 1
    assert Category.product_count == 3

def test_category_with_more_products():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("TV", "QLED 55\"", 123000.0, 7)
    p2 = Product("Monitor", "24\" FullHD", 23000.0, 12)
    c = Category("Техника", "Для дома", [p1, p2])

    assert Category.category_count == 1
    assert Category.product_count == 2
