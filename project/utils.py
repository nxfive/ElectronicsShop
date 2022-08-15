import random


def input_validation(value, var_name):
    """
        Data input validation for class object.
    """
    if var_name in ('brand', 'prod_name', 'name', 'surname'):
        if not isinstance(value, str):
            raise TypeError(f"The {var_name} value must be str. Not {type(value).__name__}.")

    if var_name in ('brand', 'name', 'surname'):
        if not value.isalpha():
            raise ValueError(f'The {var_name} value cannot include integers.')
        if not len(value) >= 3:
            raise ValueError(f'Length of {var_name} value must be equal or greater than 3.')

    if var_name == 'prod_name':
        if not value.isalnum():
            raise ValueError(f"The {var_name} value should only include alpha-numeric chars.")

    if var_name == 'net_price':
        if isinstance(value, (int, float)):
            if value < 0:
                raise ValueError(f"The {var_name} value must be positive.")
        else:
            raise TypeError(f"The {var_name} must be int or float object. Not {type(value).__name__}.")

    if var_name in ('max_capacity', 'amount_of_workers'):
        if not isinstance(value, int):
            raise TypeError(f'Value of {var_name} must be an int object. Not {type(value).__name__}.')
        if value < 0:
            raise ValueError(f'Value of {var_name} must be greater than zero!')


def create_product(class_name):
    """
        The function returns tuple with values needed to create a product instance.
    """

    def choice_attr_values(brands, products):
        brand = random.choice(brands)
        net_price = random.randint(2200, 4800)
        name = ''
        for product_list in products:
            for key, value in product_list.items():
                if key == brand:
                    name += random.choice(value)
                break
        return brand, name, net_price

    if class_name in ('Phone', 'phone'):
        create_product.phone_brand = ['SamSam', 'Nova', 'Apl', 'Elgy']
        create_product.phone_products = [
            {'SamSam': ['se20', 'se21pro', 'se21X', 'A21i', 'A10x']},
            {'Nova': ['No1c', 'No1', 'No2x', 'NokD12', 'NokC0']},
            {'Apl': ['Prod11', 'ProXc12', 'ProXc1', 'ProM1x']},
            {'Elgy': ['L1Rex', 'L2Pe', 'L23', 'L23P', 'LXp2']}
        ]
        values = choice_attr_values(create_product.phone_brand, create_product.phone_products)
        return values

    if class_name in ('Laptop', 'laptop'):
        create_product.laptop_brand = ['Eycer', 'Aply', 'Hapec', 'Leno']
        create_product.laptop_products = [
            {'Eycer': ['MT1', 'MT200', 'MaxProf1', 'MaxProf2']},
            {'Aply': ['Gamer1', 'Gamer2X', 'Ideal200', 'Ideal3X', 'NestPro1']},
            {'Hapec': ['FusionPx1', 'FXOne2', 'FXTwo3', 'FusionPro1']},
            {'Leno': ['Pro10', 'Pro11', 'Pro12', 'MaxPX10', 'MaxX4']}
        ]
        values = choice_attr_values(create_product.laptop_brand, create_product.laptop_products)
        return values


def create_worker():
    """
        The function returns tuple with values needed to create a worker instance.
    """

    create_worker.names = [
        name.rstrip() for name in open('../files/names.txt', encoding='UTF-8').readlines()
    ]
    create_worker.surnames = [
        surname.rstrip() for surname in open('../files/surnames.txt', encoding='UTF-8').readlines()
    ]

    create_worker.female_surnames = [
        surname for surname in create_worker.surnames if not surname.endswith(('ski', 'cki', 'sny', 'zki', 'y'))
    ]
    create_worker.male_surnames = [
        surname for surname in create_worker.surnames if not surname.endswith(('ska', 'cka', 'zka', 'sna', 'a'))
    ]
    choice_name = random.choice(create_worker.names)
    if choice_name.endswith('a'):
        choice_surname = random.choice(create_worker.female_surnames)
        return choice_name, choice_surname
    else:
        choice_surname = random.choice(create_worker.male_surnames)
        return choice_name, choice_surname
