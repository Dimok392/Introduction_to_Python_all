# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел
import time
def find_num(x):
    a = str(time.time())
    b = ' '
    count = 1
    while count <= x:
        b+=a[-count]
        count+=1
    return int(b)
print(int(find_num(4)))