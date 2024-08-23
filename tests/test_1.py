import pytest

from src.Category import Categoria

from src.Production import Product


class Categoria:
    total_categories = 0
    total_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Categoria.total_categories += 1

    def add_product(self, product):
        self.products.append(product)
        Categoria.total_products += product.quantity

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


@pytest.fixture
def test_category_initialization():
    category = Categoria('ананас', 'свежий и красивый')
    assert category.name == 'ананас'
    assert category.description == 'свежий и красивый'
    assert category.products == []
    assert Categoria.total_categories == 1

@pytest.fixture
def test_product_initialization():
    product = Product('ананас', 'свежий и красивый', 10.0, 5)
    assert product.name == 'ананас'
    assert product.description == 'свежий и красивый'
    assert product.price == 10.0
    assert product.quantity == 5

@pytest.fixture
def test_product_addition():
    category = Categoria('ананас', 'свежий и красивый')
    product = Product('ананас', 'свежий и красивый', 10.0, 5)
    category.add_product(product)
    assert category.products == [product]
    assert Categoria.total_products == 5

@pytest.fixture
def test_category_total_products():
    category1 = Categoria('ананас', 'свежий и красивый')
    product1 = Product('ананас', 'свежий и красивый', 10.0, 5)
    category1.add_product(product1)
    assert Categoria.total_products == 5

    category2 = Categoria('ананас', 'свежий и красивый')
    product2 = Product('ананас', 'свежий и красивый', 20.0, 10)
    category2.add_product(product2)
    assert Categoria.total_products == 15

@pytest.fixture
def test_category_total_categories():
    category1 = Categoria('ананас', 'свежий и красивый')
    assert Categoria.total_categories == 1

    category2 = Categoria('ананас', 'свежий и красивый')
    assert Categoria.total_categories == 2


