from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name} , {self.weight} , {self.category}')


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        _file = open(Shop.__file_name, 'r')
        assortment = _file.read()

        return assortment

    def add_products(self, *products):
        self.products = products
        # print(len(Shop.get_products(self)))

        if len(Shop.get_products(self)) == 0:
            for _product in products:
                _file = open(Shop.__file_name, 'a')
                _file.write(f'{_product.name} , {_product.weight} , {_product.category}\n')

        else:
            for _product in products:
                if _product.name in Shop.get_products(self):
                    pprint(f'Продукт  {_product.name}  уже есть в магазине')

                else:
                    _file = open(Shop.__file_name, 'a')
                    _file.write(f'{_product.name} , {_product.weight} , {_product.category}\n')
                    _file.close()


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
# p4 = Product('Carrot', 10, 'Vegetables')
print(p2)
# print(p4)

s1.add_products(p1, p2, p3)
# s1.add_products(p1, p2, p3, p4)
print(s1.get_products())
