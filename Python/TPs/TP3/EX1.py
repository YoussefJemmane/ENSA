list=['Lundi',2,'Janvier']
print(list)
print(list[0])
print(list[-1])
print(len(list))
list.append(2010)
print(list)
list[3] = list[3] - 1
print(list)
del list[0]
print(list)
list.insert(0,'mardi')
print(list)
print('mardi' in list)
list = [1,2,3,4,5,6,6]
num = int(input("num rechercher"))
for i in list:
    if num in list:
        print("num found in ",i)
    else:
        print("num not found")
    