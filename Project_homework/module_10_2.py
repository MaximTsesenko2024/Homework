from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        self.knight_name = name
        self.power = power
        self.count_enemy = 100
        super().__init__()

    def run(self):
        print(f"{self.knight_name}, на нас напали!", end='\n')
        day = 0
        while self.count_enemy > 0:
            sleep(1)
            self.count_enemy -= self.power
            day += 1
            print(f"{self.knight_name} сражается {day}..., осталось {self.count_enemy} воинов.", end='\n')
        print(f"{self.knight_name} одержал победу спустя {day} дней(дня)!", end='\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
