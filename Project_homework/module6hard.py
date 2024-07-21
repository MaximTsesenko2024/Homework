from math import pi, pow, sqrt


class Figure:
    sides_count = 0
    __sides = []
    __color = (0, 0, 0)
    filled = False

    def __init__(self, color, side):
        if len(side) != self.sides_count:
            side = []
            for i in range(self.sides_count):
                side.append(1)
        self.set_color(*color)
        self.set_sides(*side)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *args):
        rez = False
        if len(args) != 3:
            return rez
        for i in args:
            if not isinstance(i, int):
                return rez
            if i < 0 or i > 255:
                return rez
        rez = True
        return rez

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            color = r, g, b
            self.__color = list(color)

    def __is_valid_sides(self, *args):
        rez = False
        if len(args) == self.sides_count:
            for i in args:
                if i <= 0 or not isinstance(i, int):
                    return rez
        else:
            return rez
        rez = True
        return rez

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    __radius = 0

    def __init__(self, *args):
        if isinstance(args[0], (tuple, list)):
            color = args[0]
            side = args[1:]
        else:
            color = args[:3]
            side = args[3:]
        super().__init__(color, side)
        self.__radius = self.get_sides()[0] / pi / 2

    def get_square(self):
        return pi * pow(self.__radius, 2)


class Triangle(Figure):
    sides_count = 3
    __height = 0

    def __init__(self, *args):
        if isinstance(args[0], (tuple, list)):
            color = args[0]
            side = args[1:]
        else:
            color = args[:3]
            side = args[3:]
        super().__init__(color, side)
        self.__height = self.get_square() * 2 / max(*self.get_sides())

    def get_square(self):
        p = len(self) / 2
        a, b, c = self.get_sides()
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        return s

    def get_height(self):
        return self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, *args):
        side = []
        if isinstance(args[0], (tuple, list)):
            color = args[0]
            a = args[1:]
        else:
            color = args[:3]
            a = args[3:]
        #        self.set_color(*color)
        if len(a) > 1:
            a = (1,)
        #        self.set_sides(*side)
        for i in range(self.sides_count):
            side.append(*a)
        super().__init__(color, side)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            side = []
            for i in range(self.sides_count):
                side.append(new_sides[0])
            super().set_sides(*side)
        elif len(new_sides) == self.sides_count:
            super().set_sides(*new_sides)

    def get_volume(self):
        return pow(self.get_sides()[0], 3)


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
