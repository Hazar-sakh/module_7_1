from pprint import pprint


class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        txt = open(self.__file_name, 'r')
        file_txt = txt.read()
        txt.close()
        return file_txt

    def add(self, *products):
        lp = []
        for i in products:
            lp.append([i])
        for j in lp:
            for k in j:
                x = Shop.get_products(self)
                if k.name in x:
                    print(f'Продукт {k.name} уже есть')
                else:
                    txt = open(self.__file_name, 'a')
                    txt.write(f'{k}\n')
                    txt.close()


if __name__ in '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
