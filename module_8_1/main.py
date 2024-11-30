def add_everything_up(a, b):
    try:
        if type(a) == str or type(b) == str:
            raise Exception
    except:
        return f'{a}{b}'

    else:
        result = a + b
        return f'{result:.3f}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
