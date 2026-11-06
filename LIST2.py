# List17: Сортировка списка по возрастанию
A = list(map(int, input("Введите список чисел: ").split()))

sorted_list = sorted(A)  # Создаем отсортированную копию
print("Отсортированный список:", sorted_list)
print("Исходный список:", A)

# List19: Сортировка строк по длине
strings = input("Введите строки через пробел: ").split()

# Сортируем по длине
sorted_by_length = sorted(strings, key=len)
max_length_str = max(strings, key=len)

print("Строки по длине:", sorted_by_length)
print(f"Самая длинная строка: '{max_length_str}' (длина {len(max_length_str)})")

# List21: Положительные числа и их количество
A = list(map(int, input("Введите список чисел: ").split()))

# Генератор с фильтром
positive_numbers = [x for x in A if x > 0]
count_positive = len(positive_numbers)

print("Положительные числа:", positive_numbers)
print("Количество:", count_positive)

# List22: Умножение на D и подсчет равенств
A = list(map(int, input("Введите список чисел: ").split()))
D = int(input("Введите число D: "))

# Генератор для умножения
multiplied = [x * D for x in A]
count_equal = A.count(D)

print("Умноженные элементы:", multiplied)
print("Количество равных D:", count_equal)

# List23: Сортировка по убыванию модуля
A = list(map(int, input("Введите список чисел: ").split()))

# Сортировка по модулю в обратном порядке
sorted_by_abs = sorted(A, key=abs, reverse=True)

print("По убыванию модуля:", sorted_by_abs)

# List25: Второй по величине элемент
A = list(map(int, input("Введите список чисел: ").split()))

# Находим максимум и удаляем его
max_value = max(A)
A_copy = A.copy()
A_copy.remove(max_value)

second_max = max(A_copy)
print("Второй по величине элемент:", second_max)

# List26: Элементы больше среднего
A = list(map(int, input("Введите список чисел: ").split()))

average = sum(A) / len(A)
greater_than_avg = [x for x in A if x > average]

print("Среднее значение:", average)
print("Больше среднего:", greater_than_avg)

# List28: Строки, начинающиеся с заданной буквы
strings = input("Введите строки через пробел: ").split()
letter = input("Введите букву: ")

# Генератор для фильтрации
filtered_strings = [s for s in strings if s.startswith(letter)]

print("Строки, начинающиеся с", letter, ":", filtered_strings)

# List29: K наибольших элементов
A = list(map(int, input("Введите список чисел: ").split()))
K = int(input("Введите K: "))

# Сортировка и срез
largest_k = sorted(A, reverse=True)[:K]

print(f"{K} наибольших элементов:", largest_k)
