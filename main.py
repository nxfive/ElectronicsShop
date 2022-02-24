from worker import Worker
from customer import Customer
from shop import Shop
from laptop import Laptop
from phone import Phone


def main():
    shop = Shop('Electronic', 25, 10)
    print(shop.number_of_workers)

    # show max capacity
    shop.show_max_capacity()

    # when we change capacity of the shop we can add some products manually

    shop.max_capacity = 35
    # # create products
    laptop1 = Laptop('Leno', 'NT45', 4500)
    laptop2 = Laptop('Hpe', 'Mx123', 3450)
    laptop3 = Laptop('Apl', 'X Pro', 6000)
    phone1 = Phone('Telcom', 'A34', 3109)
    phone2 = Phone('Telxcom', 'X23', 5300)

    # when we manually create products we must add products to the shop
    # shop.add_product(laptop1)
    # shop.add_product(laptop2)
    # shop.add_product(laptop3)
    # shop.add_product(phone1)
    # shop.add_product(phone2)

    # show price of the all products in the shop
    shop.get_all_products_price()

    # # show amount of product brand
    # shop.get_amount_of_product_brand('Leno')
    #
    # # show amount of the product name
    # shop.get_amount_of_product_name('NT45')

    # show list of the all products
    shop.get_list_of_all_products()

    # create workers
    w1 = Worker(name='Marcin', surname='Kowalski')
    w2 = Worker(name='Damian', surname='Kałuża')

    # show list of workers
    Worker.display_list_of_workers()

    # create customer
    c1 = Customer(name='Piotr', surname='Kowalcze')
    # c2 = Customer(name='Kasia', surname='Maklowicz')

    # show list of customers
    Customer.display_list_of_customers()

    # add products to shopping cart
    # c1.add_to_shopping_cart('X23', shop)
    # c1.add_to_shopping_cart('A34', shop)

    # show added products
    c1.list_shopping_cart()

    # delete product from shopping cart
    c1.del_from_shopping_cart('A34')
    c1.list_shopping_cart()

    c1.pay_for_items()

    print(c1.__dict__)


if __name__ == '__main__':
    main()
