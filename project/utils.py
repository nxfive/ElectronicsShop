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

    def choice_attr_values(brand, products):
        brand = random.choice(brand)
        net_price = random.randint(2200, 4800)
        name = ''
        for item in products:
            for prod_brand, prod_names in item:
                if prod_brand == brand:
                    random.shuffle(prod_names)
                    name = prod_names[0]
        return brand, name, net_price

    if class_name in ('Phone', 'phone'):
        create_product.phone_brand = ['SamSam', 'Nova', 'Apl', 'Elgy']
        create_product.phone_products = [
            {'SamSam': ['se20', 'se21pro', 'se21X', 'A21i', 'A10x']},
            {'Nova': ['No1c', 'No', 'No2x', 'NokD12', 'NokC0']},
            {'Apl': ['Prod11', 'ProXc12', 'ProXc', 'ProM1x']},
            {'Elgy': ['L1Rex', 'L2Pe', 'L23', 'L23P', 'LXp']}
        ]
        return choice_attr_values(create_product.phone_brand, create_product.phone_products)

    if class_name in ('Laptop', 'laptop'):
        create_product.laptop_brand = ['Eycer', 'Aply', 'Hapec', 'Leno']
        create_product.laptop_products = [
            {'Eycer': ['MT1', 'MT200', 'Max Prof1', 'MaxProf2']},
            {'Aply': ['Gamer One', 'Gamer X', 'Ideal200', 'IdealX', 'Nest Pro']},
            {'Hapec': ['Fusion P', 'FX One', 'FX Two', 'Fusion Pro']},
            {'Leno': ['Pro 10', 'Pro 11', 'Pro 12', 'Max PX', 'Max X4']}
        ]
        return choice_attr_values(create_product.phone_brand, create_product.phone_products)


if __name__ == '__main__':
    create_product('phone')
