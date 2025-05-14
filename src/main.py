class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if value < self.__price:
            confirm = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {value}? (y/n): ")
            if confirm.lower() != 'y':
                print("Цена осталась без изменений.")
                return
        self.__price = value

    @classmethod
    def new_product(cls, data: dict, existing_products: list = None):
        existing_products = existing_products or []
        name = data['name']
        description = data['description']
        price = data['price']
        quantity = data['quantity']

        for product in existing_products:
            if product.name == name:
                product.quantity += quantity
                if price > product.price:
                    product.price = price
                return product

        return cls(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)

class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products or []

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]

    @property
    def product_count(self):
        return len(self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)