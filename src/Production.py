class Product:
    all_products = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise "ZeroValueError"
        if quantity < 0:
            raise "NegativeValueError"
        if quantity > 0:
            self.quantity = quantity
        else:
            self.quantity = 0


    def __add__(self, other):
        if self.name == other.name:
            self.quantity += other.quantity
            self.full_cost = self.__price * self.quantity
        else:
            raise "NameError"
        return self.full_cost, self.quantity, self.name, self.description, self.__price
