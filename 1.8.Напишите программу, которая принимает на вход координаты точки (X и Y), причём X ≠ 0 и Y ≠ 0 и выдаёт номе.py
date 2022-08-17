# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input('Введите координату x='))
y = float(input('Введите координату y='))

def get_quarter_number (x, y):
    if x != 0 and y != 0:
        if x * y > 0:
            if x > 0: return 1
            else: return 3
        else:
            if x < 0: return 2
            else: return 4
    else: 
        if x == 0: return 'OY'
        else: return 'OX'
    
print (f'Точка: {x, y}')
print (f'Четверть: {get_quarter_number(x, y)}')