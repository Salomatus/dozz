class Product:
    all_products = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = 'ананас'
        self.description = 'свежий и красивый'
        self.__price = price
        if quantity == 0:
            raise "ZeroValueError"
        if quantity < 0:
            self.quantity = quantity
        else:
            self.quantity = 0
            def __str__(self):
                return f"Product: {self.name} - {self.description} - {self.__price} - {self.quantity}"

        def __eq__(self, other):
            if self.name == other.name:
                return True
            else:
                return False
    def __hash__(self):
        return hash(self.name) + hash(self.description) + hash(self.__price) + hash(self.quantity)

    def __add__(self, other):
        if self.name == other.name:
            self.quantity += other.quantity
            self.full_cost = self.__price * self.quantity
        else:
            raise "NameError"
        return self.full_cost, self.quantity, self.name, self.description, self.__price
