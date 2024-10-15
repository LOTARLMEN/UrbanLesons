from tkinter import mainloop


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = Car.__is_valid_vin(vin)
        self.__numbers = Car.__is_valid_numbers(numbers)

    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number not in range(1000000,9999999+1):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        elif not len(numbers) == 6:
            raise IncorrectVinNumber('Неверная длина номера')
        else:
            return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')