def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for num in numbers:
        try:
            if isinstance(num, int) or isinstance(num, float) :
                (result) = result + num
            else:
                incorrect_data += 1
                raise Exception
        except:
            print(f'Некорректный тип данных для подсчета {num}')
    r = (result, incorrect_data)
    return r

def calculate_average(numbers):
    if isinstance(numbers, str):
        for num in numbers:
            print(f'Некорректный тип данных для подсчета :  {num} ')
            result = 0
        return result
    try:
        if not isinstance(numbers, list):
            raise Exception
    except:
        print('В numbers записан некорректный тип данных.')
        return 'None'

    else:
        try:
            if len(numbers) != 0:
                _res = personal_sum(numbers)
                average_result = f' {_res[0] / (len(numbers) - _res[1])}'
                return average_result
            else:
                raise Exception
        except :
            print('ZeroDivizionError \nНельзя делить на ноль')
            return 0




print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2 :{calculate_average([1, "Строка", 3, "Еще строка"])}')
print(f'Результат 3 : {calculate_average(546)}')
print(f'Результат 4 : {calculate_average([42, 15, 36, 13])}')



#print(f'Результат 5 : {calculate_average([])}')


