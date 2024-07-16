class Vehicle:
    """
    Vehicle - любое транспортное средство
    Атрибут owner(str) - владелец транспорта. (владелец может меняться)
    Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
    Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
    Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
    Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания.
    """
    owner = ''
    __model = ''
    __engine_power = 0
    __color = ''
    __COLOR_VARIANTS = ['Blue', 'Green', 'Red', 'Black', 'Yellow', 'White']

    def __init__(self, owner, model, color, enginne_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = enginne_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        def change_color(color_variants, other):
            rez = False
            if isinstance(other, str):
                for i in color_variants:
                    if i.lower() == other.lower():
                        rez = True
                        break
                return rez
            else:
                print('Неправильный тип данных.')
                return None
        if change_color(self.__COLOR_VARIANTS, new_color):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    """
    Sedan(седан) - наследник класса Vehicle
    Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)
    """
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
