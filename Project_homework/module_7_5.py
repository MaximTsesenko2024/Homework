import os
import time

directory = os.getcwd()
print(directory)
for path, dirs, files in os.walk(directory):
    for file in files:
        if os.path.isfile(file):
            filepath = os.path.join(path, file)
            parent_dir = os.path.dirname(filepath)
            size = os.path.getsize(file)
            time_ = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getatime(file)))
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {size} байт, '
                  f'Время изменения: {time_}, Родительская директория: {parent_dir}')
