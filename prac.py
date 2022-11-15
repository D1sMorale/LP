# 1 ПРЗ 11 Вариант 1 Задание
n = int(input("ВВведите количество элементов: "))
X = [int(input(f"Ввведите {i} элемент: ")) for i in range(n)]
max_elem = -float('inf')
for i in X:
    if i > max_elem and i % 2 == 0:
        max_elem = i
print(max_elem if max_elem != -float('inf') else "Нет чётных элементов")


# 1 ПРЗ 11 Вариант 2 Задание
n = int(input("ВВведите количество элементов: "))
X = [int(input(f"Ввведите {i} элемент: ")) for i in range(n)]
Y = [i for i in X if i % 2 == 0 and i < 10]
print(Y if len(Y) > 0 else "Нет чётных элементов меньше 10")


# 2 ПРЗ 11 Вариант 1 Задание
n = int(input("ВВведите n: "))
print(*[[i, i + 2] for i in range(n, 2 * n - 1)], sep='\n')


# 2 ПРЗ 11 Вариант 2 Задание
from random import randint


def arr_max_elem(arr):
    arr_max = arr[0][0]
    for i in range(len(arr)):
        if max(arr[i]) > arr_max:
            arr_max = max(arr[i])
    return arr_max


column_A, row_A, column_B, row_B = int(input("ВВведите количество столбцов матрицы А: ")), \
                                   int(input("ВВведите количество строк матрицы A: ")), \
                                   int(input("ВВведите количество столбцов матрицы B: ")), \
                                   int(input("ВВведите количество строк матрицы B: "))
A = [[randint(1, 1000) for i in range(column_A)] for j in range(row_A)]
B = [[randint(1, 1000) for i in range(column_B)] for g in range(row_B)]
print("До замены:\n")
print("Матрица A:", *A, sep="\n", end="\n\n")
print("Матрица B:", *B, sep="\n", end="\n\n")
A_max, B_max = arr_max_elem(A), arr_max_elem(B)
for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = B_max if A[i][j] == A_max else A[i][j]
for i in range(len(B)):
    for j in range(len(B[i])):
        B[i][j] = A_max if B[i][j] == B_max else B[i][j]
print("После замены:\n")
print("Матрица A:", *A, sep="\n", end="\n\n")
print("Матрица B:", *B, sep="\n", end="\n\n")


# 3 ПРЗ 11 Вариант 1 Задание
from random import randint

n = int(input('Введите размер матрицы: '))
A = [[randint(1, 1000) for i in range(n)] for j in range(n)]
print("Матрица A:", *A, sep="\n", end="\n\n")
print("сумма элементов строки, в которой расположен элемент с наименьшим значением",
      sum(A[sum(A, []).index(min(sum(A, []))) // len(A)]))


# 3 ПРЗ 11 Вариант 2 Задание
from random import randint
from math import prod
column_A, row_A, = int(input("ВВведите количество столбцов матрицы А: ")), \
                   int(input("ВВведите количество строк матрицы A: "))
A = [[randint(-10, 10) for i in range(column_A)] for j in range(row_A)]
min_prod = float('inf')
min_prod_column = []
column_index = -1
print("До замены:", *A, sep="\n", end="\n\n")
for i in range(column_A):
    temp_column = []
    for j in range(row_A):
        temp_column.append(A[j][i])
    if min_prod > prod(temp_column):
        min_prod = prod(temp_column)
        min_prod_column = temp_column
        column_index = i
for i in range(row_A):
    if column_index == 0:
        A[i][column_index], A[i][column_index+1] = A[i][column_index+1], A[i][column_index]
    else:
        A[i][column_index], A[i][column_index - 1] = A[i][column_index - 1], A[i][column_index]
print("После замены:", *A, sep="\n", end="\n\n")


# 4 ПРЗ 11 Вариант 1 Задание
try:
    with open("FIO_Gruppa_vvod.txt", 'r') as file:
        A = [[element for element in list(map(int, row.split()))] for row in file.readlines()]
    with open("FIO_Gruppa_vivod1.txt", 'w+') as file:
        file.write(str(sum(A[sum(A, []).index(min(sum(A, []))) // len(A)])))
except Exception as error:
    print("Возникла ошибка при открытии файла:", error)
    exit(-1)


# 4 ПРЗ 11 Вариант 2 Задание
from math import prod

try:
    with open("FIO_Gruppa_vvod.txt", 'r') as file:
        A = [[element for element in list(map(int, row.split()))] for row in file.readlines()]
except Exception as error:
    print("Возникла ошибка при открытии файла:", error)
    exit(-1)
row_A, column_A = len(A), len(A[0])
min_prod = float('inf')
min_prod_column = []
column_index = -1
for i in range(column_A):
    temp_column = []
    for j in range(row_A):
        temp_column.append(A[j][i])
    if min_prod > prod(temp_column):
        min_prod = prod(temp_column)
        min_prod_column = temp_column
        column_index = i
for i in range(row_A):
    if column_index == 0:
        A[i][column_index], A[i][column_index+1] = A[i][column_index+1], A[i][column_index]
    else:
        A[i][column_index], A[i][column_index - 1] = A[i][column_index - 1], A[i][column_index]
try:
    with open("FIO_Gruppa_vivod2.txt", 'w+') as file:
        for row in A:
            for element in row:
                file.write(str(element) + " ")
            file.write("\n")
except Exception as error:
    print("Возникла ошибка при открытии файла:", error)
    exit(-1)
