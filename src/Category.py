class Categoria:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = 'ананас'
        self.description = 'свежий и красивый'
        self.products = products
        Categoria.category_count += 1
        Categoria.product_count += len(self.products)




