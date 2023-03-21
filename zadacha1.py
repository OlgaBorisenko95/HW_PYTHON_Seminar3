#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint
N = int(input('Введите количество элементов масива: '))
massive = []
for i in range(N):
    massive.append(randint(1, 10))
print(massive)
X = int(input('Введите число: '))
Amount = 0
for i in massive:
    if i == X:
        Amount +=1
print(Amount)
