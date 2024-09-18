my_string = input('Введите что-либо: ')
print(f'В введённом Вами тексте {len(my_string)} символов.'
      f'\nВ введённом Вами тексте {len(my_string.replace(' ', ''))} букв.'
      f'\nВот Ваш текст в верхнем регистре: {my_string.upper()}'
      f'\nВот Ваш текст в нижнем регистре: {my_string.lower()}'
      f'\nВот Ваш текст без пробелов: {my_string.replace(' ', '')}'
      f'\nВот первый символ Вашей строки: {my_string[0]}'
      f'\nВот последний символ Вашей строки: {my_string[len(my_string)-1]}')

