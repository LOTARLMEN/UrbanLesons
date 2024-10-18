import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self, balance: int = 0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            with self.lock:
                deposit_do = randint(50, 500)
                self.balance += deposit_do
                sleep(0.001)
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
                    print(f'Пополнение: {deposit_do}. Баланс: {self.balance}.')
                    sleep(0.001)

    def take(self):
        for i in range(100):
            with self.lock:
                i = randint(50, 500)
                print(f'Запрос на {i}.')
                sleep(0.001)
                if i <= self.balance:
                    self.balance -= i
                    print(f'Снятие: {i}. Баланс: {self.balance}')
                    sleep(0.001)
                else:
                    print(f'Запрос отклонён, недостаточно средств.')
                    self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
