# Завдання 1
# def formatted_text():
#     gray_text = "Don't compare yourself with anyone in this world… "
#     red_text = "if you do so, you are insulting yourself."
#     author = "Bill Gates"
#
#     print("\033[0;37m" + gray_text)
#     print("\033[1;31mif\033[0m you \033[1;31mdo so\033[0m, you are insulting yourself.\033[0m")
#     print(author)
#
#
# formatted_text()

##############################################################################

# Завдання 2
# def even_numbers(start, end):
#     print("Парні числа між", start, "і", end, "включно:")
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             print(num, end=" ")
#
#
# start_num = int(input("Введіть початкове число: "))
# end_num = int(input("Введіть кінцеве число: "))
# even_numbers(start_num, end_num)
#
###############################################################################
#
# Завдання 3
# def draw_square(side_length, symbol, filled):
#     if filled:
#         for _ in range(side_length):
#             print(symbol * side_length)
#     else:
#         print(symbol * side_length)
#         for _ in range(side_length - 2):
#             print(symbol + " " * (side_length - 2) + symbol)
#         print(symbol * side_length)
#
#
# side_length = int(input("Введіть довжину сторони квадрата: "))
# symbol = input("Введіть символ для квадрата: ")
# filled = input("Заповнений квадрат? (y/n): ").lower() == "y"
# draw_square(side_length, symbol, filled)
#
#################################################################################
#
# Завдання 4
# def find_minimum(num1, num2, num3, num4, num5):
#     return min(num1, num2, num3, num4, num5)
#

# num1 = float(input("Введіть перше число: "))
# num2 = float(input("Введіть друге число: "))
# num3 = float(input("Введіть третє число: "))
# num4 = float(input("Введіть четверте число: "))
# num5 = float(input("Введіть п'яте число: "))
#
# minimum = find_minimum(num1, num2, num3, num4, num5)
# print("Мінімальне число: ", minimum)
#
##################################################################################
#
# Завдання 5
# def product_in_range(num1, num2):
#     if num1 > num2:
#         num1, num2 = num2, num1
#     product = 1
#     for num in range(num1, num2 + 1):
#         product *= num
#     return product
#
# lower_bound = int(input("Введіть нижню межу діапазону: "))
# upper_bound = int(input("Введіть верхню межу діапазону: "))
#
# result = product_in_range(lower_bound, upper_bound)
# print("Добуток чисел у вказаному діапазоні:", result)
#
##################################################################################
#
# Завдання 6
# def count_digits(number):
#     return len(str(number))
#
#
# number = int(input("Введіть число: "))
#
# digits_count = count_digits(number)
# print("Кількість цифр у числі:", digits_count)
#
##################################################################################
#
# Завдання 7
# def is_palindrome(number):
#     num_str = str(number)
#     return num_str == num_str[::-1]
#
# number = int(input("Введіть число: "))
# if is_palindrome(number):
#     print("Число", number, "є паліндромом")
# else:
#     print("Число", number, "не є паліндромом")
#
###################################################################################
