import pytest

from src.Category import Category

from src.Production import Product


@pytest.fixture()
def category_test():
    return Category('ананас', 'свежий и красивый', [])


def category_init_test(category):
    assert category.name == 'ананас'
    assert category.description == 'свежий и красивый'
    assert category.products_counter == 1


@pytest.fixture
def product_test():
    return Product('ананас', 'свежий и красивый', 10.0, 3)


def product_init_test(product_test):
    assert product_test.name == 'ананас'
    assert product_test.description == 'свежий и красивый'
    assert product_test.price == 10.0
    assert product_test.quantity == 3
    assert product_test.full_cost == 30.0


def test_price(product_test):
    product_test.price = 10.0
    assert product_test.price == 10

    product_test.price = 15.0
    assert product_test.price == 15.0



