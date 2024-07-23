class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def add(self, *products):
        list_ = self.get_products()
        file = open(self.__file_name, 'a')
        for i in products:
            if not (i.name in list_):
                file.write(str(i)+'\n')
                list_ += str(i)
            else:
                print(f'Продукт {i.name} уже есть в магазине')
        file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        list_ = file.read()
        file.close()
        return list_


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
