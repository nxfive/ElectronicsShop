from project.shop.shop import Shop
from project.person.customer import Customer
from project.utils.utils import create_customer
import random


def main():
    shop = Shop('Electronic', 20, 5)
    for i in range(10):
        customer = Customer(shop, *(create_customer()))
        customer.make_action(random.randint(1, 5))
    revenue = 0
    for product in shop._sold_products:
        revenue += product.price_with_margin - product.net_price

    print(f'Shop sold {len(shop._sold_products)} products, earned: {revenue}')


if __name__ == '__main__':
    main()
