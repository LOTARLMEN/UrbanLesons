def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(int(input('Введите целое натуральное число'
                               ' колличества строк матрицы: ')), int(input('Введите целое натуральное число'
                                                                           'колличества столбцов: ')), input('Введие '
                                                                                                             'значение заполнения'
                                                                                                             'матрицы: '))

print(result1)
