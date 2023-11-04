num1 = [[1,2,3],[4,5,6],[7,8,9]]
num2 = [[10,11,12],[13,14,15],[16,17,18]]
num3 = []


for i in num1:
    print(i[0],num2[0])
    num3.append([i[0],num2[0]])
    
print(num3)
print(num3[0][1])

for j in num3[0]:
    print(j[0])


