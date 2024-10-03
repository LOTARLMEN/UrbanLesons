def cipher(first_field):
    if first_field in range(3, 21):
        password_ = []
        for i in range(1, first_field):
            for j in range(1, first_field):
                if first_field % (i + j) == 0 and i < j:
                    password_.append(f"{i}{j}")
        return ''.join(password_)
    else:
        return 'Вы ввели не правильное число!!!'

print(cipher(int(input('Введите число от 3 до 20: '))))