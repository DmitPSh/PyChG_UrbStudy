def get_matrix(row, column, value):
    matrix =[]
    row_=[]
    column_ =[]

    for i in range(row):
        matrix.append(row_)
        row = row-1
        column_ = value
        for j in range(column):
            row_.append(column_)
            column=column-1


    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print (result1)
print (result2)
print (result3)