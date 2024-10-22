from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number: int, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))




class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}.')
                    guest.start()
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди.')


    def discuss_guests(self):
        while True:
            for table in self.tables:
                if (table.guest is not None) and not table.guest.is_alive():
                    table.guest.join()
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла).')
                    print(f'Стол номер {table.number} свободен.')
                    table.guest = None
                    break
                elif table.guest is None and not self.queue.empty():
                    some_guest = self.queue.get()
                    table.guest = some_guest
                    print(f'{some_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}.')
                    some_guest.start()
                    break
            if self.queue.empty() and all(table.guest is None for table in self.tables):
                break

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()