# Proc2: Функция для вычисления степеней
def power_a234(a):
    return a**2, a**3, a**4

# Ввод пяти чисел
numbers = list(map(float, input("Введите 5 чисел через пробел: ").split()))

# Обработка каждого числа
for num in numbers:
    a2, a3, a4 = power_a234(num)
    print(f"Число {num}: 2-я степень = {a2}, 3-я степень = {a3}, 4-я степень = {a4}")

# Proc4: Функция для треугольника
import math

def triangle_ps(a):
    perimeter = 3 * a
    area = (a**2 * math.sqrt(3)) / 4
    return perimeter, area

# Ввод трёх сторон
sides = list(map(float, input("Введите 3 стороны треугольника: ").split()))

# Обработка каждой стороны
for side in sides:
    p, s = triangle_ps(side)
    print(f"Сторона {side}: Периметр = {p}, Площадь = {s}")

# Proc5: Функция для прямоугольника
def rect_ps(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    perimeter = 2 * (width + height)
    area = width * height
    return perimeter, area

# Ввод координат трёх прямоугольников
print("Введите координаты для 3 прямоугольников (x1 y1 x2 y2):")
for i in range(3):
    coords = list(map(float, input(f"Прямоугольник {i+1}: ").split()))
    p, s = rect_ps(*coords)
    print(f"Прямоугольник {i+1}: Периметр = {p}, Площадь = {s}")

# Proc7: Функция переворота цифр
def invert_digits(k):
    return int(str(k)[::-1])

# Ввод пяти чисел
numbers = list(map(int, input("Введите 5 чисел: ").split()))

# Обработка каждого числа
for num in numbers:
    print(f"Число {num} -> {invert_digits(num)}")

# Proc8: Функция добавления цифры справа
def add_right_digit(d, k):
    return int(str(k) + str(d))

# Ввод данных
K = int(input("Введите число K: "))
D1 = int(input("Введите D1: "))
D2 = int(input("Введите D2: "))

# Первый шаг
result1 = add_right_digit(D1, K)
print(f"Шаг 1: {K} + {D1} = {result1}")

# Второй шаг
result2 = add_right_digit(D2, result1)
print(f"Шаг 2: {result1} + {D2} = {result2}")

# Proc9: Функция добавления цифры слева
def add_left_digit(d, k):
    return int(str(d) + str(k))

# Ввод данных
K = int(input("Введите число K: "))
D1 = int(input("Введите D1: "))
D2 = int(input("Введите D2: "))

# Первый шаг
result1 = add_left_digit(D1, K)
print(f"Шаг 1: {D1} + {K} = {result1}")

# Второй шаг
result2 = add_left_digit(D2, result1)
print(f"Шаг 2: {D2} + {result1} = {result2}")

# Proc11: Функция сравнения
def minmax(x, y):
    return min(x, y), max(x, y)

# Ввод четырёх чисел
A, B, C, D = map(float, input("Введите 4 числа: ").split())

# Первый вызов: сравниваем A и B
min1, max1 = minmax(A, B)

# Второй вызов: сравниваем C и D
min2, max2 = minmax(C, D)

# Третий вызов: находим общий минимум
final_min, _ = minmax(min1, min2)

# Четвёртый вызов: находим общий максимум
_, final_max = minmax(max1, max2)

print(f"Минимум среди чисел: {final_min}")
print(f"Максимум среди чисел: {final_max}")

# Proc13: Функция сортировки трёх чисел
def sort_dec3(a, b, c):
    # Создаём список и сортируем его
    numbers = [a, b, c]
    numbers.sort(reverse=True)
    return numbers[0], numbers[1], numbers[2]

# Обработка двух наборов чисел
for i in range(2):
    print(f"\nНабор {i+1}:")
    a, b, c = map(float, input("Введите три числа: ").split())
    sorted_a, sorted_b, sorted_c = sort_dec3(a, b, c)
    print(f"Отсортированный набор: {sorted_a}, {sorted_b}, {sorted_c}")

# Proc14: Функция правого сдвига
def shift_right3(a, b, c):
    return b, c, a

# Обработка двух наборов
for i in range(2):
    print(f"\nНабор {i+1}:")
    a, b, c = map(float, input("Введите три числа: ").split())
    new_a, new_b, new_c = shift_right3(a, b, c)
    print(f"После сдвига: {new_a}, {new_b}, {new_c}")

# Proc15: Функция левого сдвига
def shift_left3(a, b, c):
    return c, a, b

# Обработка двух наборов
for i in range(2):
    print(f"\nНабор {i+1}:")
    a, b, c = map(float, input("Введите три числа: ").split())
    new_a, new_b, new_c = shift_left3(a, b, c)
    print(f"После сдвига: {new_a}, {new_b}, {new_c}")
