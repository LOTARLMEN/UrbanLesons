my_dict = {'Ktun' : 1998, 'Marika' : 1111, 'Krushak' : 1}

print(f'Словарь: {my_dict}'
      f'\nЗначение пары с ключом "Thrall" которого нет: {my_dict.get('Thrall')}'
      f'\nЗначение пары с ключом "Ktun"\n{my_dict.get('Ktun')}')

delited_ = my_dict.pop('Ktun')

print(f'Нынешний словарь: {my_dict}'
      f'\nЗначение удалённой пары: {delited_}'
      f'\n')

my_set = {156, 156, 223, 1984, 'Ага', 'Ага'}
print(f'Множество: {my_set}')
my_set.add('Рык')
my_set.add(512)
print(f'Новое множество: {my_set}')
print(f'Множество с удалённым элементом')