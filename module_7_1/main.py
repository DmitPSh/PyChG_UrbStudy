
from pprint import pprint
import  os

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self ):
        return (f'{self.name} , {self.weight} , {self.category}')

class Shop( ):
    __file_name = 'products.txt'
    def __init__(self):
        pass
    def get_products(self):
        global content
        file = open(self.__file_name, 'r', encoding='utf-8')
        content = file.read()
        if content:
            return content
        else:
            return " "
        file.close()
    def add_products(self, *products):
        if os.stat("products.txt").st_size == 0:
            for product in products:
                _file = open(self.__file_name, 'a', encoding='utf-8')
                _file.write(f'{product.name}, {product.weight}, {product.category}, \n')
                _file.close()
        else:

            for product in products:
                if str(product) not in self.get_products():
                    _file = open(self.__file_name, 'a', encoding='utf-8')
                    _file.write(f'{product.name}, {product.weight}, {product.category}, \n')
                    _file.close()
                else:
                    print(f'Продукт {product.name} уже есть в магазине.')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add_products(p1 ,p2 ,p3)
print(s1.get_products())





