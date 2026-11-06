# Err2: Чтение двух целых чисел и вывод частного
try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    result = a / b
    print(f"{result:.1f}")  # Вывод с одним знаком после точки
except ZeroDivisionError:
    print("Делить на ноль нельзя")

# Err5: Получение символа по индексу
try:
    text = input("Введите строку: ")
    index = int(input("Введите индекс: "))
    print(text[index])
except IndexError:
    print("Нет такого символа")

# Err6: Расширенная обработка ошибок для индекса
try:
    text = input("Введите строку: ")
    index = int(input("Введите индекс: "))
    print(text[index])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")

# Err7: Ввод числа с проверкой
while True:
    try:
        number = int(input("Введите число: "))
        break  # Если ввод успешный, выходим из цикла
    except ValueError:
        print("Это не число. Попробуй ещё:")
print(f"Получено число: {number}")

# Err9: Проверка возраста
try:
    age = int(input("Введите возраст: "))
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
except ValueError as e:
    print(f"Отклонено: {e}")
else:
    print(f"Принято: {age}")

# Err11: Деление с обработкой ошибок
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = a / b
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{result:.2f}")  # Вывод с двумя знаками после точки

# Err12: Обработка ошибок с выводом типа
try:
    number = int(input("Введите целое число: "))
    print(f"Получено число: {number}")
except Exception as e:
    print(f"Сообщение об ошибке: {e}")
    print(f"Тип ошибки: {type(e).__name__}")
