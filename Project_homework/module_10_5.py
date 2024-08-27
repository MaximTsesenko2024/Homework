import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name) as file:
        line = file.readline()
        while line != '':
            all_data.append(line)
            line = file.readline()


if __name__ == '__main__':
    files = [f'./file {i}.txt' for i in range(1, 5)]
    start = datetime.now()
    for file in files:
        read_info(file)
    end = datetime.now()
    print('Линейный метод ', end - start)
    with multiprocessing.Pool(processes=6) as pool:
        start = datetime.now()
        pool.map(read_info, files)
    end = datetime.now()
    print('Многопроцессорный метод ', end - start)
