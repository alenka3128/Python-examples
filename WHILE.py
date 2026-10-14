# While2
# Даны положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). Не используя операции умножения и деления, найти количество отрезков B, размещённых на отрезке A.
A = int(input())
B = int(input())

count = 0
current = A

while current >= B:
    current -= B
    count += 1

print(count)

# While4
# Дано целое число N (> 0). Если оно является степенью числа 3, то вывести TRUE, если не является — вывести FALSE
N = int(input())

temp = N

while temp % 3 == 0:
    temp //= 3

if temp == 1:
    print("TRUE")
else:
    print("FALSE")

# While5
# Дано целое число N (> 0), являющееся некоторой степенью числа 2: N = 2^K. Найти целое число K — показатель этой степени
N = int(input())

k = 0
temp = N

while temp > 1:
    temp //= 2
    k += 1

print(k)

# While6
# Дано целое число N (> 0). Найти двойной факториал N: N!! = N·(N−2)·(N−4)·… (последний сомножитель равен 2, если N — чётное, и 1, если N — нечётное). Вычислять произведение с помощью вещественной переменной и вывести как вещественное число
N = int(input())

result = 1.0
current = N

while current > 0:
    result *= current
    current -= 2

print(result)

# While7
# Дано целое число N (> 0). Найти наименьшее целое положительное число K, квадрат которого превосходит N: K² > N. Функцию извлечения квадратного корня не использовать
N = int(input())

K = 1
while K * K <= N:
    K += 1

print(K)

# While9
#  Дано целое число N (> 1). Найти наименьшее целое число K, при котором выполняется неравенство 3^K > N.
N = int(input())

power_of_3 = 1
K = 0

while power_of_3 <= N:
    power_of_3 *= 3
    K += 1

print(K)

# While10
#  Дано целое число N (> 1). Найти наибольшее целое число K, при котором выполняется неравенство 3^K < N.
N = int(input())
power_of_3 = 1
K = 0

while power_of_3 * 3 < N:
    power_of_3 *= 3
    K += 1

print(K)

# While12
# Дано целое число N (> 1). Вывести наибольшее из целых чисел K, для которых сумма 1 + 2 + … + K будет меньше или равна N, и саму эту сумму.
N = int(input())

total = 0
K = 0

while True:
    next_k = K + 1
    if total + next_k > N:
        break
    K = next_k
    total += K

print(K, total)

# While13
#  Дано число A (> 1). Вывести наименьшее из целых чисел K, для которых сумма 1 + 1/2 + … + 1/K будет больше A, и саму эту сумму.
A = float(input())

total = 0.0
K = 0

while total <= A:
    K += 1
    total += 1 / K

print(K, total)

# While14 
# Дано число A (> 1). Вывести наибольшее из целых чисел K, для которых сумма 1 + 1/2 + … + 1/K будет меньше A, и саму эту сумму.
A = float(input())

total = 0.0
K = 0

while True:
    next_k = K + 1
    next_total = total + 1 / next_k
    if next_total >= A:
        break
    K = next_k
    total = next_total

print(K, total)