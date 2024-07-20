#Задача "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.
# Пункты задачи:
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0
first = input("Input first integer: ")
while type(first) != int:
    try:
        first = int(first)
    except ValueError:
        print("It's not an integer, try again")
        first = input("Input first integer: ")
second = input("Input second integer: ")
while type(second) != int:
    try:
        second = int(second)
    except ValueError:
        print("It's not an integer, try again")
        second = input("Input second integer: ")
third = input("Input third integer: ")
while type(third) != int:
    try:
        third = int(third)
    except ValueError:
        print("It's not an integer, try again")
        third = input("Input third integer: ")
if first == second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')




