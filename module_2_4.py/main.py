
#list_=[1, 2, 3, 4, 5, 6, 7]
list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []

for i in range(len(list_) -1, 1, -1):
     for j in range( 1, len(list_)-1):
          if (j < i):
               if list_[i] % list_[j] == 0:
                        print('number', list_[i],  '= sdhgjhgjprime')
                        prime.append(list_[i])
                        break
               else:
                        print('number', list_[i],  '= not_prime')
                        not_prime.append(list_[i])
                        break

# for i in range(2,len(list_)):
#      print('list [',i,']=',list_[i])
#      for j in range(1, len(list_)):
#           if list[i] % list[j] != 0:
#                print('number', list[i],  '= prime')
#                prime.append(list[i])
#                break
#
#
#           else:
#                print('number', list[i],  '= not_prime')
#                not_prime.append(list[i])
#                break

print(not_prime)
print(prime)

