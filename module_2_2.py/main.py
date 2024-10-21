first = input('Введите первое целое число: ')
second = input('Введите второе целое число: ')
third = input('Введите третье целое число: ')

print('Вы ввели: ', first, second, third, ' соответственно')

if first == second and first == third:
    print('Результат:', 3)
elif first != second  and first == third  or first == second and first != third:
    print('Результат:', 2)
else:
    print('Результат:', 0)
