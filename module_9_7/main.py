def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(2, result):
            if result % i == 0:
                return 'Составное'
            else:
                return  "Простое"
        return result
    return wrapper



@is_prime
def sum_three(a, b, c):
    return (a+b+c)
print (sum_three(2,3, 6))
#print (sum_three(83,100, 200))
#print (sum_three(86,311, 600))

def sum_three(a, b, c):
    return a+b+c
print(sum_three(2, 3, 6))
#print (sum_three(83,100, 200))
#print (sum_three(86,311, 600))