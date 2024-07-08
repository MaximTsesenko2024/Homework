class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor in range(1, self.number_of_floors + 1):
            for i in range(1, new_floor + 1):
                print(f'Этаж номер: {i}')
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print('Неправильный тип данных. Необходим тип House.')
            return None

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print('Неправильный тип данных. Необходим тип House.')
            return None

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('Неправильный тип данных. Необходим тип House.')
            return None

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print('Неправильный тип данных. Необходим тип House.')
            return None

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('Неправильный тип данных. Необходим тип House.')
            return None

    def __ne__(self, other):
        if isinstance(other, House):
            return not (self.number_of_floors == other.number_of_floors)
        else:
            print('Неправильный тип данных. Необходим тип House.')
            return None

    def __add__(self, other: int):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            print('Неправильный тип данных. Необходим тип Int.')
            return None

    def __radd__(self, other: int):
        return self.__add__(other)

    def __iadd__(self, other: int):
        return self.__add__(other)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
