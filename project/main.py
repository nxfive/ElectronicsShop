import asyncio

from project.shop.shop import Shop
from project.person.customer import Customer
from project.utils.utils import create_customer
from project.database.database import *
import random
import time
from statistics import mean

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


async def create_process_async(delay, number):
    await asyncio.sleep(delay)
    shop = Shop(create_db(_data[number][0]), *(_data[number]))
    for i in range(5):
        customer = Customer(shop, *(create_customer()))

        customer.make_action(random.randint(1, 5))
    revenue = 0
    for product in shop.sold_products_by_instance:
        revenue += product.price_with_margin - product.net_price
    sold = len(shop.sold_products_by_instance)
    earned_all = [item.price_with_margin - item.net_price for item in shop.sold_products_all]
    print(f'Shop {shop.name} sold {sold} products, earned: {revenue}')
    print(f'All shops sold {len(shop.sold_products_all)} products, earned: {sum(earned_all)}')
    return shop.name, revenue, sold


async def process():
    start = time.time()
    # zero_task = list(asyncio.all_tasks())[0]
    tasks = set()
    for r in range(0, 5):
        task = asyncio.create_task(create_process_async(random.randint(0, 4), r))
        tasks.add(task)
        # task.add_done_callback(tasks.discard)
    # tasks = asyncio.all_tasks() - {zero_task}
    for task in tasks:
        # returns = await asyncio.gather(asyncio.to_thread(task), return_exceptions=True)
        await asyncio.gather(asyncio.to_thread(task), return_exceptions=True)

        # print(returns)
    end = time.time()
    return end - start


def create_process(delay, number):
    time.sleep(delay)
    shop = Shop(create_db(_data[number][0]), *(_data[number]))

    for i in range(5):
        customer = Customer(shop, *(create_customer()))
        customer.make_action(random.randint(1, 5))
    revenue = 0
    for product in shop.sold_products_by_instance:
        revenue += product.price_with_margin - product.net_price
    sold = len(shop.sold_products_by_instance)
    earned_all = [item.price_with_margin - item.net_price for item in shop.sold_products_all]
    print(f'Shop {shop.name} sold {sold} products, earned: {revenue}')
    print(f'All shops sold {len(shop.sold_products_all)} products, earned: {sum(earned_all)}')
    return shop.name, revenue, sold


def process2():
    start = time.time()
    result = []
    for r in range(0, 5):
        result.append(create_process(random.randint(0, 4), r))
    print(result)
    end = time.time()
    return end - start


def main():
    result = []
    result_async = []
    for i in range(10):
        result_async.append(asyncio.run(process()))
    for i in range(10):
        result.append(process2())

    print(f"Average time func with async: {mean(result_async)}")
    print(f"Average time func without async: {mean(result)}")


main()

