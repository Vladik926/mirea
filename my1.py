№1.3
x = 5 >= 2
A = {1, 3, 7, 8}
B = {2, 4, 5, 10, 'apple'}
C = A & B

df = ['Антонова Антонина', 34, 'ж']
z = 'type'  # Строка z
D = [1, 'title', 2, 'content']

print("x:", x, "Тип:", type(x))
print("A:", A, "Тип:", type(A))
print("B:", B, "Тип:", type(B))
print("C:", C, "Тип:", type(C))
print("df:", df, "Тип:", type(df))
print("z:", z, "Тип:", type(z))
print("D:", D, "Тип:", type(D))
Ответ:
x: True Тип: <class 'bool'>
A: {8, 1, 3, 7} Тип: <class 'set'>
B: {2, 4, 5, 10, 'apple'} Тип: <class 'set'>
C: set() Тип: <class 'set'>
df: ['Антонова Антонина', 34, 'ж'] Тип: <class 'list'>
z: type Тип: <class 'str'>
D: [1, 'title', 2, 'content'] Тип: <class 'list'>

№2.3
x = float(input("Введите значение x: "))

if x < -5:
    print("x принадлежит интервалу (-∞, -5)")
elif -5 <= x <= 5:
    print("x принадлежит интервалу [-5, 5]")
else:
    print("x принадлежит интервалу (5, +∞)")
  ответ:
Введите значение x: 3
x принадлежит интервалу [-5, 5]


№3.31
x = 10
while x >= 1:
    print(x)
    x -= 3

ответ:
10
7
4
1
№3.32
characteristics = [
    "Возраст",
    "Пол",
    "Рост",
    "Вес",
    "Цвет волос",
    "Цвет глаз",
    "Уровень образования",
    "Профессия",
    "Место проживания",
    "Хобби",
    "Семейное положение",
    "Национальность",
    "Язык общения",
    "Здоровье",
    "Социальный статус"
]

# Вывод списка на экран
for characteristic in characteristics:
    print(characteristic)


ответ:
Возраст
Пол
Рост
Вес
Цвет волос
Цвет глаз
Уровень образования
Профессия
Место проживания
Хобби
Семейное положение
Национальность
Язык общения
Здоровье
Социальный статус




№3.33
x = 2
while x <= 15:
    print(x)
    x += 1


ответ:
2
3
4
5
6
7
8
9
10
11
12
13
14
15


№3.34
for i in range(106, 5, -25):
    print(i)

ответ:
106
81
56
31
6




№4.35:
import math


def calculator():
    print("Простой калькулятор")
    print("Введите два числа (x и y):")

    x = float(input("Введите x: "))
    y = float(input("Введите y: "))

    print("\nВыберите действие:")
    print("1. Сложение (x + y)")
    print("2. Вычитание (x - y)")
    print("3. Умножение (x * y)")
    print("4. Деление (x / y)")
    print("5. e^(x + y)")
    print("6. sin(x + y)")
    print("7. cos(x + y)")
    print("8. x^y")

    choice = input("\nВведите номер действия (1-8): ")

    if choice == '1':
        result = x + y
        print(f"Результат: {x} + {y} = {result}")
    elif choice == '2':
        result = x - y
        print(f"Результат: {x} - {y} = {result}")
    elif choice == '3':
        result = x * y
        print(f"Результат: {x} * {y} = {result}")
    elif choice == '4':
        if y != 0:
            result = x / y
            print(f"Результат: {x} / {y} = {result}")
        else:
            print("Ошибка: Деление на ноль!")
    elif choice == '5':
        result = math.exp(x + y)
        print(f"Результат: e^({x} + {y}) = {result}")
    elif choice == '6':
        result = math.sin(x + y)
        print(f"Результат: sin({x} + {y}) = {result}")
    elif choice == '7':
        result = math.cos(x + y)
        print(f"Результат: cos({x} + {y}) = {result}")
    elif choice == '8':
        result = x ** y
        print(f"Результат: {x} ^ {y} = {result}")
    else:
        print("Ошибка: Неверный номер действия!")


if __name__ == "__main__":
    calculator()


ответ:
Простой калькулятор
Введите два числа (x и y):
Введите x: 25
Введите y: 2

Выберите действие:
1. Сложение (x + y)
2. Вычитание (x - y)
3. Умножение (x * y)
4. Деление (x / y)
5. e^(x + y)
6. sin(x + y)
7. cos(x + y)
8. x^y

Введите номер действия (1-8): 8
Результат: 25.0 ^ 2.0 = 625.0

Process finished with exit code 0



