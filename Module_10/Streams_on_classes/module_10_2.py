from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        while True:
            if self.enemies == 0:
                print(f'{self.name} одержал победу!')
                break
            else:
                sleep(1)
                self.days += 1
                self.enemies -= self.power
                print(f'{self.name}, сражается {self.days} день(дня), осталось врагов: {self.enemies}\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

threads = [first_knight, second_knight]

first_knight.start()
second_knight.start()

for thread in threads:
    thread.join()

print('Все битвы кончились!')