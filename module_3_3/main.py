
print('\t\t Функция с параметрами по умолчанию ')

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c )

print_params()
print_params(13, c = False)
print_params(b = 'Текст')

print_params(b = 25)
print_params(c = [1,2,3])

print('\t\t Распаковка параметров ')

values_list = ['документ', 33, 10.1]
values_dict = dict(a = 22, b = 7, c = 'h')

print_params(*values_list)
print_params(**values_dict)

print('\t\t Распаковка + отдельные параметры ')

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
