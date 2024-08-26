import queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

    def set_guest(self, guest=None):
        self.guest = guest

    def get_guest(self):
        return self.guest

    def empty(self):
        return self.guest is None

    def get_number(self):
        return self.number


class Guest(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        sleep(randint(3, 10))

    def __str__(self):
        return self.name


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        def find_empty_table():
            for table in self.tables:
                if table.empty():
                    return table
            return None

        for guest in guests:
            table = find_empty_table()
            if table is None:
                self.queue.put(guest)
                print(f"{guest} в очереди")
            else:
                table.set_guest(guest)
                print(f"{guest} сел(-а) за стол номер {table.get_number()}")
                guest.start()

    def discuss_guests(self):
        def find_all_empty():
            for table in self.tables:
                if not table.empty():
                    return False
            return True

        stop = find_all_empty() and self.queue.empty()
        while not stop:
            for table in self.tables:
                if not table.empty():
                    guest = table.get_guest()
                    if guest.is_alive():
                        print(f"{guest} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.get_number()} свободен")
                        table.set_guest()
                        if not self.queue.empty():
                            guest = self.queue.get()
                            table.set_guest(guest)
                            print(f"{guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.get_number()}")
                            guest.start()
            stop = find_all_empty() and self.queue.empty()


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
