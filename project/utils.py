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
