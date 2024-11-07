class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
     return (f'Название:{self.name}, кол-во этажей:{self.number_of_floors}  ')



    def go_to(self,  new_floor):
        if  new_floor <= self.number_of_floors and new_floor >= 1:
            for i in range(1, new_floor + 1):
                print(i)
        else:
                print("Такого этажа не существует")

# Модуль _5_3 (Задача "Нужно больше этажей")
# Для решения этой задачи будем пользоваться решением к
# предыдущей задаче "Специальные методы класса".

    def __eq__(self, other):
        if isinstance(other,House):
            return self.number_of_floors == other.number_of_floors
        else:
            print('Error : this is not an object of type House')
    def __add__(self, value):

        if isinstance(value, int):
            self.number_of_floors  += value
            return  self.number_of_floors
        else:
            print('Error : this is not an object of type Integer')

    def __gt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors > other.number_of_floors
        else:
            print('Error : this is not an object of type House')
    def __ge__(self, other):
        if isinstance(other,House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('Error : this is not an object of type House')
    def __lt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors < other.number_of_floors
        else:
            print('Error : this is not an object of type House')
    def __le__(self, other):
        if isinstance(other,House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('Error : this is not an object of type House')

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print('Error : this is not an object of type House')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

#__str__
print(h1)
print(h2)



print(House.__eq__(h1, h2))
House.__add__(h1, 10)
print(h1)
print(House.__eq__(h1, h2))
House.__add__(h1, 10)
print(h1)
House.__add__(h2, 10)
print(h2)
print(House.__gt__(h1, h2))
print(House.__ge__(h1, h2))
print(House.__lt__(h1, h2))
print(House.__le__(h1, h2))
print(House.__ne__(h1, h2))




