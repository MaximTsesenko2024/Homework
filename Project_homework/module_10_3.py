from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            add = randint(50, 500)
            self.balance += add
            print(f"Пополнение: {add}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            sub = randint(50, 500)
            print(f"Запрос на {sub}")
            if sub > self.balance:
                self.lock.acquire()
                print("Запрос отклонён, недостаточно средств")
            else:
                self.balance -= sub
                print(f"Снятие: {sub}. Баланс: {self.balance}")
                sleep(0.001)


bank = Bank()
th1 = Thread(target=Bank.deposit, args=(bank,))
th2 = Thread(target=Bank.take, args=(bank,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый баланс: {bank.balance}")
