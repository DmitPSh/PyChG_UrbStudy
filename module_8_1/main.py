def add_everything_up(a, b):
    try:
        if type(a) == str or type(b) == str:
            raise Exception
    except:
        return f'{a}{b}'

    else:
        result = a + b
        return result


print(add_everything_up(123, 'fghj'))
print(add_everything_up('fghj', 456.7))
print(add_everything_up(123.56, 76.44))
