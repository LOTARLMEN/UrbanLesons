first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(fst) - len(scd) for fst, scd in zip(first, second) if len(fst) != len(scd))
second_result = (len(first[i]) == len(second[i]) for i in range(3))

print(list(first_result))
print(list(second_result))