'''
Задача 1: Валидация пароля

Пользователь хочет установить пароль для своей учетной записи. Пароль должен соответствовать следующим критериям:

    Длина пароля должна быть не менее 8 символов.
    Пароль должен содержать хотя бы одну заглавную букву (A-Z).
    Пароль должен содержать хотя бы одну строчную букву (a-z).
    Пароль должен содержать хотя бы одну цифру (0-9).
    Пароль должен содержать хотя бы один специальный символ из множества: !@#$%^&*()_-+=<>?/

Напишите программу, которая запрашивает у пользователя пароль и затем проверяет, удовлетворяет ли он всем критериям. Если пароль удовлетворяет всем критериям, программа должна сообщить, что пароль принят. В противном случае, программа должна вывести сообщение об ошибке, указывая, какие критерии не выполняются.

'''

# password = input('Введите пароль из 8 символов: ')

# zaglav = [x for x in password if x.isupper()]
# mal = [x for x in password if x.islower()]
# symbol = [x for x in password if x in '!@#$%^&*()_-+=<>?/']
# cifra = [x for x in password if x.isdigit()]
# if len(password) < 8:
#     raise ValueError ('Длина пароля должна быть не менее 8 символов')
# if len(zaglav) == 0:
#     raise ValueError ('Пароль должен содержать хотя бы одну заглавную букву (A-Z)')
# if len(mal) == 0:
#     raise ValueError ('Пароль должен содержать хотя бы одну строчную букву (a-z)')
# if len(symbol) == 0:
#     raise ValueError ('Пароль должен содержать хотя бы один специальный символ из множества: !@#$%^&*()_-+=<>?/')
# if len(cifra) == 0:
#     raise ValueError ('Пароль должен содержать хотя бы одну цифру (0-9)')
# else:
#     print('Пароль принят!')

'''
Задача 2: Обработка ошибок при работе с элементами списка:

Создайте список чисел и попробуйте выполнить некоторые операции над элементами списка. Обработайте исключения, такие как IndexError, ValueError и ZeroDivisionError.
'''

# numbers = (2, 3, 4, 5, 6, 7, 8, 9)

# for i in numbers:
#     try:
#         y = int(input())
#         x = i + y
#     except IndexError as e:
#         print(f'IndexError: {e}')
#     except ValueError as e:
#         print(f'ValueError: {e}')
#     except ZeroDivisionError as e:
#         print(f'ZeroDivisionError: {e}')
#     except Exception as e:
#         print({e})
#     else:
#         print({x})
#     finally:
#         print('Финал')

'''
Задача 3: Поиск значения в словаре с обработкой исключения:

Создайте словарь с данными (например, словарь с именами и возрастами людей). Затем запросите у пользователя имя и попробуйте найти возраст этой персоны в словаре. Обработайте исключение, если имя не найдено.
'''

# try:
#     names = {'Annie': 25, 'Jame': 30, 'Alex': 40, 'Steve': 35}

#     user_name = input('Enter your name: ')

#     # Поиск возраста в словаре
#     if user_name in names:
#         age = names[user_name]
#         print(f'The age of {user_name} is {age}.')
#     else:
#         print(f'Sorry, {user_name} not found in the dictionary.')

# except Exception as e:
#     print(f'An error occurred: {e}')