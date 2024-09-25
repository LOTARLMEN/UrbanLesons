numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    for j in range(2, int(i**0.5) + 1):
        if i % j != 0:
            primes.append(i)

        else:
            not_primes.append(i)
        break


print(f'Простые числа: {primes}'
      f'\nНе простые числа: {not_primes}')