#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint
N = int(input('Введите количество элементов масива: '))
massive1, massive2 = [], []
for i in range(N):
    massive1.append(randint(1, 10))
print(massive1)
X = int(input('Введите число: '))
for i in massive1:
    massive2.append(abs(X-i))
print(massive1[massive2.index(min(massive2))])
