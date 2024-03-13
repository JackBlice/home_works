'''
1) Создайте функцию, которая генерирует рандомное (случайно сгенерированное) число и выводит на окно терминала через команду print(). Далее создайте декоратор, который журналирует это событие. То есть функция декоратор должна писать в dict() предложение: «Функция …………… была запущена успешно», а ключом будет уникальный идентификатор (id).   (10 баллов)
'''
# from random import randint

# def decor(func1):
#     def wrapper(*args, **kwargs):
#         print(f'Функция {func1.__name__} была заупущена успешно')
#         func1()

#     return wrapper


# @decor
# def func():
#     num_id = randint(1, 32433)
#     print(num_id)

# func()

'''
2) Напишите функцию, которая принимает фразу, и возвращает его сокращенную форму.
Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest -- FYI и т.п. (10 баллов)
'''

# def socrashenie():
#     fraza = input('Vvedite frazu: ').split()
#     res = ''
#     for i in fraza:
#         res += i[0].upper()
#     return res

# print(socrashenie())

'''
3) Напишите декоратор, который проверяет, что функция вызывается с определенными типами аргументов. (15 баллов)
'''

# def decorator(func):
#     def wrappers(*args, **kwargs):
#         try:
#             for i in args:
#                 if type(i) == int:
#                     print('U vas vse normalno')
#                 else:
#                     raise ValueError
#         except ValueError:
#             print('U vas oshibka ')
#     return wrappers


# @decorator
# def proverka(a, b):
#     return

# proverka(5, 6)

'''
4) Создайте декоратор, который автоматически преобразует результат функции в другой тип данных, (15 баллов)
'''

# def deco(dannye):
#     def wrapper(*args, **kwargs):
#         print(type(dannye(*args, **kwargs)))
#         print(type(str(dannye(*args, **kwargs))))

#     return wrapper
        

# @deco
# def func(a, b, c):
#     return a + b + c

# func(3, 4, 5)

'''
5) Реализуйте декоратор, который ограничивает максимальное количество вызовов функции. (20 баллов)
'''

# def vyzov(limit):
#     def decorator(func):
#         calls = 0

#         def wrapper(*args, **kwargs):
#             nonlocal calls
#             if calls < limit:
#                 calls += 1
#                 return func(*args, **kwargs)
#             else:
#                 print(f"Максимальное количество вызовов функции {func.__name__} достигнуто.")
#         return wrapper
#     return decorator



# @vyzov(3)
# def greet(name):
#     print(f"Привет, {name}!")

# greet("Анна")
# greet("Боб")
# greet("Карл")
# greet("Джон")

'''
6) Напишите декоратор, который автоматически логирует исключения, возникающие внутри функции. (15 баллов)
'''

# def decor(func):
#     def wrapper(*args, **kwargs):
#         try:
#             print(func(*args, **kwargs))
#         except:
#             print('Ошибка выловилась!')
#     return wrapper


# @decor
# def func(a, b, c):
#     return a + b + c

# func(3, 4, 5)

'''
7) Напишите декоратор, который ограничивает доступ к функции только определенным пользователям или ролям. (15 баллов) 
'''
# names = {
#     'James': 'Director',
#     'Bob': 'Manager',
#     'Elsa': 'Employee'
# }

# def decor(functions):
#     def wrapper(*args, **kwargs):
#         name = input()
#         role = input()
#         for n in names.items():
#             if name in n or role in n:
#                 return (functions(*args, **kwargs))
#         ('Вам длоступ запрещен!')
#     return wrapper




# @decor
# def func(a, b, c):

#     return a + b + c

# print(func(3, 4, 5))