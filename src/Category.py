class Category:
    categories_set = set()
    categories_counter = 0
    products_set = set()
    products_counter = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        self.full_cost = 0
        self.prod_number = 0

        Category.categories_set.add(self.name)
        Category.categories_counter = len(Category.categories_set)

        for x in self.__products:
            Category.products_set.add(x.name)
        Category.products_counter = len(Category.products_set)

