from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'at')
        for i in data_set:
            file.write(str(i) + '\n')
        file.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке', (1,3,4,5)])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
second_ball = MysticBall('Первый', 'Третий', 'Девятый', 'Сотый')
print(second_ball())
print(second_ball())
print(second_ball())
print(second_ball())
