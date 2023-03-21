# Дан список чисел. Определите, сколько в нем встречается различным чисел.
# Ввод [1, 1, 2, 0, -1, 3, 4, 4]
# Вывод 6

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