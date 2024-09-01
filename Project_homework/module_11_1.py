from matplotlib import pyplot as plt
import numpy as np


x = np.arange(-4, 4, 0.1)  # генерация массива чисел от -4 до 4 с интервалом 0.1
y1 = np.sin(x)  # генерация массива значений функции синус
y2 = np.cos(x)  # генерация массива значений функции косинус
y = np.append(y1, y2)  # обединение массивов
y = y.reshape((2, 80))  # изменение формы массива без изменения количества элементов
fig, ax = plt.subplots(figsize=(5, 2))
ax.plot(x, y[0], label='y=sin(x)')  # добавление данных для отображения
ax.plot(x, y[1], label='y=cos(x)')  # добавление данных для отображения
ax.set_title('Графики функций y=sin(x), y=cos(x)')  # задание заголовка графика
ax.legend(loc='lower right')  # определение расположения подписи графиков
ax.set_ylabel('y')  # задание названия оси y
ax.set_xlabel('x')  # задание названия оси x
ax.vlines(np.arange(-4, 4, 0.5), ymin=-1, ymax=1, colors='b')  # добавление сетки по оси x
ax.hlines(np.arange(-1, 1, 0.25), -4, 4, colors='g')  # добавление сетки по оси y
plt.show()  # вывод фигуры на экран
