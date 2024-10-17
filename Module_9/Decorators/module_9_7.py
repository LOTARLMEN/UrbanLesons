def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if all(result % i != 0 for i in range(2, int(result**0.5)+1)):
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*nums):
    return sum(nums)

print(sum_three(2, 3, 6))