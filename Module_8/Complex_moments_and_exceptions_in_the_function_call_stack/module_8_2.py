def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for num in numbers:
        if isinstance(num, (int, float)):
            result += num
        else:
            print(f'Некорректный тип данных для подсчёта суммы - {num}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    if isinstance(numbers, str):
        # Если передана строка, разбиваем её на символы
        numbers = list(numbers)

    if not isinstance(numbers, (list, tuple)):
        print(f'В numbers записан некорректный тип данных')
        return None

    result, incorrect_data = personal_sum(numbers)
    total_numbers = len(numbers) - incorrect_data

    if total_numbers > 0:
        return result / total_numbers
    else:
        return 0

    # Примеры тестов


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')