'''
Задание 1.
Есть список list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]

 

     Написать функцию которая будет принимать этот список в качестве аргумента. Далее функция должна ВЕРНУТЬ список состоящий из имен(строковых значений) и чтобы эти имена были с заглавной буквы и в алфавитном порядке
    Написать функцию которая будет принимать этот список в качестве аргумента. Далее функция должна ВЫВЕСТИ НА КОНСОЛЬ список из целочисленных значений в отсортированном виде но в обратном порядке, т.е от большого к маленькому
    Написать функцию которая будет принимать этот список в качестве аргумента. Далее функция должна ВЕРНУТЬ сложение всех чисел с плавающей точкой
'''

# list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]

# def names(list_1):
#     ls_names = []
#     for x in list_1:
#         if str == type(x):
#             ls_names.append(x.title())
#     return sorted(ls_names)

# print(names(list_1))

# def ls_second(list_1):
#     ia = []
#     for i in list_1:
#         if int == type(i):
#             ia.append(i)
#     return sorted(ia)[::-1]
    
# print(ls_second(list_1))


# def ls_third(list_):
#     count = 0
#     for i in list_1:
#         if float == type(i):
#             count += i
#     return (count)

# print(ls_third(list_1))

# ------------------------------------------

# def ls_third(num):
#     num = [float(x) for x in num]
#     count = 0
#     for i in num:
#         if float == type(i):
#             count += i
#     return (count)
# ky = input('ca: ').split()
# print(ls_third(ky))

'''
Задание 2.
Сэндвичи: напишите функцию, которая получает первым аргументом размер сэндвича в виде строкового значения и список компонентов сэндвича.

При вызове функции, функция должна выводить описание заказанного сэндвича например «Большой сэндвич со следующими ингредиентами: огурец, колбаса … » . Вызовите функцию три раза с разными количествами аргументов и разными размерами (Большой, средний, маленький)
'''

# def sandwich1(arg, list_):
#         if arg == '1':
#             print(f'Большой сэндвич со следующими ингредиентами: {list_}')
#         elif arg == '2':
#             print(f'Средний сэндвич со следующими ингредиентами: {list_}')
#         elif arg == '3':
#             print(f'маленький сэндвич со следующими ингредиентами: {list_}')

# while True:
#     sizes = input('Размер сендвича: \n\nБольшой(1)   Средний(2)   Маленький(3)  Выход(4): ')
#     ingredients = input('Игнгрединеты для сендвича: ')
    
#     if sizes == 'выход' or ingredients == 'выход':
#          break
#     else:
#         sandwich1(sizes, ingredients)

'''
Задание 3.
Напишите функцию для сохранения информации об автомобиле в словаре . Функция всегда должна возвращать производителя и название модели, но при этом она может получать произвольное количество именованных аргументов . Вызовите функцию с передачей обязательной информации и еще двух пар «имя—значение» (например, цвет и комплектация) . Ваша функция должна работать для вызовов следующего вида: car = make_car(‘subaru’, ‘outback’, colour=’blue’, engine='V8') и возвращать строку" Subaru Outback colour is blue, engine is V8
'''

# def make_car(mark, model, engine, **kwargs):

#     for key, values in kwargs.items():
#         print(f'{mark} {model} {key} is {values} , engine is {engine}')
        
        
# make_car('subary', 'forester','V8', colour = 'blue')

'''
Задача 4

Напишите функцию count_letters, которая принимает на вход текст и подсчитывает, какое в нём количество цифр и букв. Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.

Реализовать в цикле while, для выхода пользователь должен ввести "выход"

Пример:

Введите текст: 100 лет в обед

Какую цифру ищем? 0

Какую букву ищем? л

 

Количество цифр 0: 2

Количество букв л: 1
'''

# def count_letters(text,digit,letter):
#     count1 = 0
#     count2 = 0
#     for i in text:
#         if digit == i:
#             count1 += 1
#         elif letter == i:
#             count2 += 1
   
#     print(f'Количество цифр {digit}:{count1} ')
#     print(f'Количество букв {letter}:{count2} ')


# count_letters(user_text,search_digits_in_user_text, search_letters_in_user_text)

'''
Задача 5.

Напишите функцию, которая в виде аргумента принимает словарь (данные с именами и должностями , где ключ это имя работника,  а значение его должность. Функция должна вернуть предложения, типа:  
Работник Асан, занимает должность Директор
'''
# names = {
#     'Sanzhar': 'Mentor',
#     'Anvar': 'Tech Support'
# }
# def slovar(name):
#     for key,value in name.items():
#         print(f'Rabotnik: {key}, Doljnost {value}')
# slovar(names)

'''
Задача 6 (дополнительно)

Напишите программу, которая будет суммировать все числа, введенные пользователем, игнорируя при этом нечисловой ввод. Выводите на экран текущую сумму чисел после каждого очередного ввода. Ввод пользователем значения, не являющегося числовым, должен приводить к появлению соответствующего предупреждения, после чего пользователю должно быть предложено ввести следующее число. Выход из программы будет осуществляться путем пропуска ввода. Удостоверьтесь, что ваша программа корректно обрабатывает целочисленные значения и числа с плавающей запятой. 

Пример:

Введите число: 1

Сумма: 1

Введите число: 2

Сумма: 3

Введите число: 5

Сумма: 8

Введите число: кукарача

Ошибка, введите только числа

Введите число: 12

Сумма: 20 (т.е. сумма не обнуляется, а продолжает "считать" (8 + 12 = 20)
'''

# def numbers():
#     count = 0
#     while True:
#         try:
#             num_one = float(input('Введите число: '))
#             if num_one == 0:
#                 break
#         except ValueError:
#             print('Ты ввел неправильные данные!')
#             continue
#         else:
#             count += num_one
#         print(count)

# numbers()









