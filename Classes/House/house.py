class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def __eq__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

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

if __name__ == '__main__':
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h1.go_to()
    h2.go_to()