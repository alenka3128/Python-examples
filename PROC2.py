def roots_count(a, b, c):
    if a == 0:
        raise ValueError("Коэффициент a не должен быть равен нулю")
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        return 2
    elif discriminant == 0:
        return 1
    else:
        return 0

# Обработка трёх уравнений
for i in range(3):
    print(f"\nУравнение {i+1}:")
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
    count = roots_count(a, b, c)
    print(f"Количество корней: {count}")

def circle_s(r):
    return 3.14 * r**2

# Обработка трёх кругов
for i in range(3):
    radius = float(input(f"\nКруг {i+1}: введите радиус: "))
    area = circle_s(radius)
    print(f"Площадь круга: {area:.2f}")

import math

def triangle_p(a, h):
    b = math.sqrt((a/2)**2 + h**2)
    return a + 2*b

# Обработка трёх треугольников
for i in range(3):
    print(f"\nТреугольник {i+1}:")
    base = float(input("Введите основание a: "))
    height = float(input("Введите высоту h: "))
    perimeter = triangle_p(base, height)
    print(f"Периметр: {perimeter:.2f}")

def sum_range(a, b):
    if a > b:
        return 0
    return sum(range(a, b+1))

# Ввод и обработка
A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

sum_ab = sum_range(A, B)
sum_bc = sum_range(B, C)

print(f"Сумма от {A} до {B}: {sum_ab}")
print(f"Сумма от {B} до {C}: {sum_bc}")

def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        raise ValueError("Координаты не должны быть нулевыми")

# Обработка трёх точек
for i in range(3):
    print(f"\nТочка {i+1}:")
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    q = quarter(x, y)
    print(f"Точка находится в {q}-й четверти")

def even(k):
    return k % 2 == 0

# Обработка набора из 10 чисел
numbers = list(map(int, input("Введите 10 чисел через пробел: ").split()))
count_even = sum(even(num) for num in numbers)
print(f"Количество чётных чисел: {count_even}")

def is_square(k):
    if k <= 0:
        return False
    root = int(k**0.5)
    return root * root == k

# Обработка набора из 10 чисел
numbers = list(map(int, input("Введите 10 положительных чисел: ").split()))
count_squares = sum(is_square(num) for num in numbers)
print(f"Количество квадратов: {count_squares}")

def is_power5(k):
    if k <= 0:
        return False
    while k % 5 == 0:
        k = k // 5
    return k == 1

# Обработка набора из 10 чисел
numbers = list(map(int, input("Введите 10 положительных чисел: ").split()))
count_powers = sum(is_power5(num) for num in numbers)
print(f"Количество степеней пятёрки: {count_powers}")

def is_power_n(k, n):
    if k <= 0 or n <= 1:
        return False
    while k % n == 0:
        k = k // n
    return k == 1

# Ввод данных
n = int(input("Введите основание n (> 1): "))
numbers = list(map(int, input("Введите 10 положительных чисел: ").split()))

count_powers = sum(is_power_n(num, n) for num in numbers)
print(f"Количество степеней числа {n}: {count_powers}")

def digit_count(k):
    if k <= 0:
        raise ValueError("Число должно быть положительным")
    return len(str(k))

# Обработка пяти чисел
for i in range(5):
    number = int(input(f"Введите число {i+1}: "))
    digits = digit_count(number)
    print(f"Число {number} содержит {digits} цифр")
