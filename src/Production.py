class Product:
    all_products = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise "ZeroValueError"
        else:
            self.quantity = quantity
        self.full_cost = self.__price * self.quantity

        Product.all_products.append(self)
        super().__init__()
