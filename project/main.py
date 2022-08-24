import asyncio

from project.shop.shop import Shop
from project.person.customer import Customer
from project.utils.utils import create_customer
from project.database.database import *
import random

_data = [
    ('Electronic', 20, 5),
    ('MediaMax', 40, 8),
    ('ExpertRTV', 32, 6),
    ('ComputerM', 25, 6),
    ('TeleMarkt', 30, 4),
]


def create_db(item):
    db = Database(f"{item.lower()}.db")
    create_database(db)
    return db


async def create_process(number):
    shop = Shop(create_db(_data[number][0]), *(_data[number]))

    for i in range(5):
        customer = Customer(shop, *(create_customer()))
        customer.make_action(random.randint(1, 5))
    revenue = 0
    for product in shop._sold_products_by_instance:
        revenue += product.price_with_margin - product.net_price
    sold = len(shop._sold_products_by_instance)
    earned_all = [item.price_with_margin - item.net_price for item in shop._sold_products_all]
    print(f'Shop {shop.name} sold {sold} products, earned: {revenue}')
    print(f'All shops sold {len(shop._sold_products_all)} products, earned: {sum(earned_all)}')
    return shop.name, revenue, sold


async def main():
    # zero_task = list(asyncio.all_tasks())[0]
    tasks = []
    for r in range(0, 5):
        tasks.append(asyncio.create_task(create_process(r)))
    # tasks = asyncio.all_tasks() - {zero_task}
    returns = await asyncio.gather(*tasks, return_exceptions=True)
    print(returns)

asyncio.run(main())
