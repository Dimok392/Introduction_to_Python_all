# 5.Задайте список из n чисел последовательности (1+1\n)^n и выведите на экран их сумму

def sum_posl(x):
    s = 0
    sum = 0
    for i in range (1, x+1):
        s = (1+1/i)**i
        sum=sum+s
        print(s, end=' ')
    print( )
    print(f'Сумма чисел последовательности = {sum}')
num = int(input('Введите число: '))
sum_posl(num)


# 5.Задайте список из n чисел последовательности 3n+1 и выведите на экран их сумму
# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# def sum_posl(x):
#     s = 0
#     sum = 0
#     for i in range (1, x+1):
#         s = 3*i+1
#         sum=sum+s
#         print(s, end=' ')
#     print( )
#     print(f'Сумма чисел последовательности = {sum}')
# num = int(input('Введите число: '))
# sum_posl(num)