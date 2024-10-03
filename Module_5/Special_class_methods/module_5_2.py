class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def go_to(self):
        while True:
            try:
                new_floor = int(input(f'Введите номер этажа, на который вы собираетесь переехать в здании "{self.name}"'
                                      f'с колличеством этажей {self.number_of_floors}: '))
                if new_floor > self.number_of_floors or new_floor <= 0:
                    print(f'Невозможно переехать на {new_floor} этаж в этом здании!!! Его не существует!!!')
                    continue
                else:
                    for i in range(1, new_floor + 1):
                        print(i)
                break
            except ValueError:
                print("Как вы планируете переехать на подобный этаж? Это даже не целое число!!!")

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))