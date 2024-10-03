immutable_var = (1, 2, 3, 'слон')
print(immutable_var)
# immutable_var[0] = "2"
# print(immutable_var)
# программа выдаёт ошибку "'tuple' object does not support item assignment" - Кортежи не поддерживают
# изменение подобных элементов
mutable_list = ([1, 2], 'омепразол')
print(mutable_list)
mutable_list[0][0] = 'яблоко'
print(mutable_list)

