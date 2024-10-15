def add_everything_up(number, string):
    try:
        return number + string
    except TypeError:
        return f'{number}{string}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))