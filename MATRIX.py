# Matrix2: Сформировать матрицу M × N, у которой все элементы J-го столбца равны 5·J (J = 1, ..., N)
M = int(input("Введите M: "))
N = int(input("Введите N: "))

A = [[5 * (j + 1) for j in range(N)] for i in range(M)]

for row in A:
    print(*row)

# Matrix3: Даны M, N и набор из M чисел. Сформировать матрицу, у которой
# в каждом столбце содержатся все числа набора в том же порядке
M = int(input("Введите M: "))
N = int(input("Введите N: "))
A = list(map(float, input(f"Введите {M} чисел: ").split()))

# Матрица: в каждой строке i стоит A[i], то есть каждый столбец — весь набор
matrix = [[A[i] for _ in range(N)] for i in range(M)]

for row in matrix:
    print(*row)

# Matrix5: Даны M, N, число D и набор из M чисел. Первый столбец — набор;
M = int(input("Введите M: "))
N = int(input("Введите N: "))
D = float(input("Введите D: "))
first = list(map(float, input(f"Введите {M} чисел: ").split()))

matrix = []
for i in range(M):
    row = [first[i] + D * j for j in range(N)]
    matrix.append(row)

for row in matrix:
    print(*row)

# Matrix6: Даны M, N, число Q и набор из N чисел. Первая строка — набор;
M = int(input("Введите M: "))
N = int(input("Введите N: "))
Q = float(input("Введите Q: "))
first = list(map(float, input(f"Введите {N} чисел: ").split()))

matrix = []
current = first[:]          
for i in range(M):
    matrix.append(current[:])  
    current = [x * Q for x in current]   

for row in matrix:
    print(*row)

# Matrix10: Вывести элементы столбцов с нечётными номерами (1, 3, ...)
# по столбцам, без условного оператора
M = int(input("Введите M: "))
N = int(input("Введите N: "))
matrix = [list(map(float, input(f"Строка {i+1}: ").split())) for i in range(M)]
for j in range(0, N, 2):
    column = [matrix[i][j] for i in range(M)]
    print("Столбец", j + 1, ":", *column)

