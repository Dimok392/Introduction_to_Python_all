# 1.Программа принемает на вход число N и выдаёт последовательность из N членов 

# Пример для N = 5: 1,-3,9,-27,81

# def searchNumber(a, b):
#      my_lists = [1]
#      while len(my_lists) < a:
#           my_lists.append(my_lists[-1]*b)
#           print(my_lists)

# searchNumber(5, -3)

def searchNumber(x):
    s = 1
    print(s, end=' ')
    for i in range (1, x):
        s = s*-3
        print(s, end= ' ')


searchNumber(5)
