class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__color = list(color)
        self.__sides = sides
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return (isinstance(r, int) and 0 <= r <= 255 and
                isinstance(g, int) and 0 <= g <= 255 and
                isinstance(b, int) and 0 <= b <= 255)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = True

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in list(sides)) and len(sides) == len(self.__sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *radius):
        super().__init__(color, radius)
        if self.sides_count == len(radius):
            self.__radius = radius[0]
            self._Figure__sides = list(radius)
        else:
            self._Figure__sides = [1] * self.sides_count

    def get_square(self):
        return (self.__radius ** 2) * 3.14

    def __len__(self):
        return self.__radius

    def set_sides(self, *new_sides):
        self.__radius = new_sides[0]
        self._Figure__sides = list(new_sides)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if self.sides_count == len(sides):
            self._Figure__sides = [side for side in sides]
            self.sides = sides
        elif len(sides) == 1:
            self._Figure__sides = [sides[0] for _ in range(self.sides_count)]
        else:
            self._Figure__sides = [1] * self.sides_count

    def get_square(self):
        p = 0.5 * sum(self.get_sides())
        a, b, c = self.get_sides()
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if self.sides_count == len(sides):
            self._Figure__sides = [side for side in sides]
            self.side = self._Figure__sides[0]
        elif len(sides) == 1:
            self._Figure__sides = [sides[0] for _ in range(self.sides_count)]
            self.side = sides[0]
        else:
            self._Figure__sides = [1] * self.sides_count

    def get_volume(self):
        return 6 * self.side * self.side


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
