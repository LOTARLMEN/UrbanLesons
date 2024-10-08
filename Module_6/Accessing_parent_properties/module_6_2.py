class Vehicle:
    __PASSENGERS_LIMIT = 5
    __COLOR_VARIANTS = ['red', 'blue', 'green', 'black', 'white']

    def __init__(self, owner, __model,__color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color


class Sedan(Vehicle):

    def get_model(self):
        return f"Модель: {self._Vehicle__model}"
    def get_horsepower(self):
        return f"Мощность двигателя: {self._Vehicle__engine_power}"
    def get_color(self):
        return f"Цвет: {self._Vehicle__color}"
    def print_info(self):
        print(f'{self.get_model()}\n'
              f'{self.get_horsepower()}\n'
              f'{self.get_color()}\n'
              f'Владелец: {self.owner}')
    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self._Vehicle__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

if __name__ == '__main__':
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()

