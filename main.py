

class Category:
    """Класс для категорий """

    name: str
    description: str
    __goods: list  # приватный атрибуд

    # общее количество категорий и общее количество уникальных продуктов
    number_of_categories = 0
    number_of_unique_products = 0

    def __init__(self, name, description):
            """Метод для инициализации экземпляра класса, задаем значение атрибутам экземпляра"""
            self.name = name
            self.description = description
            self.__goods = []  # Инициализируем список товаров

            Category.number_of_categories += 1
            Category.number_of_unique_products += 1

    def add_product(self, product):
            """Метод для добавления товара в список товаров"""
            self.__goods.append(product)

    @property
    def goods(self):
            goods_info = []
            for product in self.__goods:
                goods_info.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
                return goods_info


class Production:
    """Класс для продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса, задаем значение атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.__price = price  # приватный атрибут
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        """Класс-метод для создания товара и возращения объекта"""
        return cls(name, description, price, quantity)

    @classmethod
    def create_product1(cls, name, description, price, quantity, products_list):
        for existing_product in products_list:
            if existing_product.name == name:
                if existing_product.price < price:
                    existing_product.price = price
                existing_product.quantity += quantity
                return None
        new_product = cls(name, description, price, quantity)
        products_list.append(new_product)
        return new_product

    if __name__ == '__main__':
        main()
