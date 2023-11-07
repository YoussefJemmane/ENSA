num1 = [[1,2,3],[4,5,6],[7,8,9]]
num2 = [[10,11,12],[13,14,15],[16,17,18]]
num3 = []


for i in range(len(num1)):
    temp = []
    for j in range(len(num2[0])):
        print(i,j)
        temp.append(0)
    num3.append(temp)

    for j in range(len(num2)):
        for k in range(len(num2[0])):
            num3[i][j] += num1[i][k] * num2[k][j]

print(num3)