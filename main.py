from src.Category import Category


from src.Production import Product


def main(load_data=None):
    data = load_data
    list_category = []
    for unit in data:
        list_product = [un for un in unit["products"]]

    class Category:
        category_count = 0
        product_count = 0

        def __init__(self, name: str, description: str, products: list = None) -> None:
            self.name = name
            self.description = description
            self.products = products
            Category.category_count += 1
            Category.product_count += len(self.products)

        result = []
        for element in list_product:
            product = Product(element["name"], element["description"],
                              element["price"], element["quantity"])
            result.append(f'{product.get_product_name()}\n'
                          f'{product.get_product_description()}\n'
                          f'{product.get_product_price()}\n'
                          f'{product.get_product_quantity_in_stock()}\n\n'
                          )
            print(list_category)

            if __name__ == '__main__':
                main()