def calculate_structure_sum(*data):
    total_sum = 0

    for item in data:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, dict):
            total_sum += calculate_structure_sum(*item.keys())
            for value in item.values():
                if isinstance(value, (list, tuple)):
                    total_sum += calculate_structure_sum(*value)
                elif isinstance(value, dict):
                    total_sum += calculate_structure_sum(*value.keys())
                    total_sum += calculate_structure_sum(*value.values())
                elif isinstance(value, int):
                    total_sum += value
        elif isinstance(item, (list, tuple)):
            total_sum += calculate_structure_sum(*item)
        elif isinstance(item, set):
            total_sum += calculate_structure_sum(*list(item))
    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(*data_structure))