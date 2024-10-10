num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Primes = [2]
Not_Primes = []


for i in range(2, len(num)):
    print('               ',num[i], 'это число    ',  i, '-это индекс  ')

    for j in range( 1, len(num)-1):
        print(num[i] % num[j])
        if num[i] % num[j] == 0:
            print('Not_Primes')
            Not_Primes.append(num[i])
            break

        else:
            print('Primes')
            Primes.append(num[i])
            break

print(Primes)
print(Not_Primes)
