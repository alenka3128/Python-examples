# List2: Вывести A[K], последний элемент и число элементов перед K
A = list(map(int, input("Введите список чисел: ").split()))
K = int(input("Введите индекс K: "))

print(f"Элемент A[{K}]: {A[K]}")
print(f"Последний элемент: {A[-1]}")
print(f"Элементов перед A[{K}]: {K}")

# List3: Сумма и произведение элементов с чётными индексами
A = list(map(int, input("Введите список чисел: ").split()))

sum_even = 0
prod_even = 1

for i in range(0, len(A), 2):
    sum_even += A[i]
    prod_even *= A[i]

print(f"Сумма элементов с чётными индексами: {sum_even}")
print(f"Произведение элементов с чётными индексами: {prod_even}")

# List5: Добавить элемент D в конец списка
A = list(map(int, input("Введите список чисел: ").split()))
D = int(input("Введите число D: "))

A.append(D)
print(f"Новый список: {A}")
print(f"Длина списка: {len(A)}")

# List7: Вывести элементы в обратном порядке
A = list(map(int, input("Введите список чисел: ").split()))

print("Обратный порядок:")
print(A[::-1])  # или A.copy().reverse()
print("Исходный список:")
print(A)

# List9: Элементы больше среднего арифметического
A = list(map(int, input("Введите список чисел: ").split()))

average = sum(A) / len(A)
result = [x for x in A if x > average]

print(f"Элементы больше среднего: {result}")
print(f"Количество таких элементов: {len(result)}")

# List10: Поиск самой длинной и короткой строки
strings = input("Введите строки через пробел: ").split()

min_str = min(strings, key=len)
max_str = max(strings, key=len)

print(f"Самая короткая строка: '{min_str}' (длина {len(min_str)})")
print(f"Самая длинная строка: '{max_str}' (длина {len(max_str)})")

# List12: Вставка 0 по индексу K
A = list(map(int, input("Введите список чисел: ").split()))
K = int(input("Введите индекс K: "))

A.insert(K, 0)
print(f"Новый список: {A}")
print(f"Длина списка: {len(A)}")

# List13: Удаление последнего элемента
A = list(map(int, input("Введите список чисел: ").split()))

removed = A.pop()
print(f"Удаленный элемент: {removed}")
print(f"Полученный список: {A}")

# List14: Поиск вхождений числа D
A = list(map(int, input("Введите список чисел: ").split()))
D = int(input("Введите число D: "))

count = A.count(D)
index = A.index(D) if D in A else -1

print(f"Число вхождений: {count}")
print(f"Индекс первого вхождения: {index}")

# List15: Элементы на нечётных позициях (с 1)
A = list(map(int, input("Введите список чисел: ").split()))

# Позиции считаются с 1, поэтому берём чётные индексы (1, 3, 5...)
odd_elements = A[1::2]
sum_odd = sum(odd_elements)
