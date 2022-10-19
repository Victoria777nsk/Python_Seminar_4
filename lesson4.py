'''
27. Задайте строку из набора чисел. Запишите ее в файл. Напишите программу, которая считает строку из файла и покажет 
большее и меньшее число. В качестве символа-разделителя используйте пробел.
'''
# string = '12 -5 34 71 -74 39 0'
# with open('task_27.txt', 'w') as f:
#     f.write(string)

# with open('task_27.txt') as file:
#     my_str = file.read()          # Читаем и сохраняем в новую строку (чтобы можно было работать с ней дальше).

# def find_max_min(str_1):
#     my_list = [int(x) for x in str_1.split()]  # Проходим по списку и оборачиваем элементы строки в тип int.
#     print(my_list)
#     return min(my_list), max(my_list)

# # new_str = '12374 12 65 '
# a, b = find_max_min(my_str)
# # print(a, b)

# if a > b:
#     print(f'Наибольшее число = {a}')
#     print(f'Наименьшее число = {b}')
# else:
#     print(f'Наибольшее число = {b}')
#     print(f'Наименьшее число = {a}')


'''
28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
 - с помощью математических формул нахождения корней квадратного уравнения
 - с помощью дополнительных библиотек Python
При этом функцию для нахождения дискриминанта импортируйте из файла utils.py

'''

# from utils import discr
# from math import sqrt

# a = int(input('Введите число A: '))
# b = int(input('Введите число B: '))
# c = int(input('Введите число C: '))

# def Quadratic_Equation(a,b,c):
#     dis = discr(a, b, c)
#     print(f'D = {dis}')
    
#     if dis < 0:
#         print('Корней нет')
#     elif dis == 0:
#         x = round(-b / 2 * a, 2)
#         print(x = {x})
#     else:
#         x1 = round((-b - sqrt(dis)) / (2 * a), 2)
#         x2 = round((-b + sqrt(dis)) / (2 * a), 2)
#         print(f'x1 = {x1}, x2 = {x2}')
# Quadratic_Equation(a,b,c)


# # from math import sqrt
# # import math

# # def find_roots(a, b, c):
# #     D = b ^ 2 - 4 * a * c
# #     roots = []
# #     if D < 0:
# #         roots.append('Нет корней')
# #         return roots
# #     x1 = (-b + math.sqrt(D)) / (2 * a)
# #     roots.append(x1)
# #     if D > 0:
# #         x2 = (-b - math.sqrt(D)) / (2 * a)
# #         roots.append(x2)
# #     return roots

# # a, b, c = 1, -2, 8
# # print(find_roots(a, b, c))

# # from utils import discr

# # def find_roots(a, b, c):
# #     D = discr(a, b, c)
# #     roots = []
# #     x1 = (-b + D ** 0.2) / (2 * a)
# #     roots.append(x1)
# #     x2 = (-b - D ** 0.5) / (2 * a)
# #     roots.append(x2)
# #     return set(roots)

# # a, b, c = 4, 4, 15
# # print(find_roots(a, b, c))


'''
29.
Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
Это наименьшее натуральное число, которое делится и на «а», и на «b». 
Например: у нас есть два целых числа 4 и 6. 
Найдем НОК: Кратные 4: 4, 8, 12, 16, 20, 24, 28, 32, 36,... 
Кратные 6: 6, 12, 18, 24, 30, 36, 42,...
Общие кратные 4 и 6 — это просто числа, которые есть в обоих списках: 12, 24, 36, 48, 60, 72,.... 
НОК — это наименьший общий множитель, поэтому он равен 12.

'''

# def calculate_lcm(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while True:
#         if (greater % x == 0) and (greater % y == 0):
#             lcm = greater   # lcm = НОК
#             break
#         greater += 1
#     return lcm

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))

# print(f'НОК чисел {num1} и {num2} = {calculate_lcm(num1, num2)}')

# # from math import lcm, gcd
# #
# # def get_lcm(a, b):
# #     return lcm(a, b)
# #
# #
# # print(f'НОК чисел {num1} и {num2} равен {get_lcm(num1, num2)}')
# #
# # print(f'НОД чисел {num1} и {num2} равен {gcd(num1, num2)}')


# # import math

# #
# # help(math)


# # A = 1
# # B = -8
# # C = 12
# #
# # from utils import discr as ds
# # from  math import sqrt
# # x1 = -B- sqrt(ds(A, B, C))/2*A
# # x2 = -B + sqrt(ds(A, B, C))/2*A
# #
# # print(x1, x2)
