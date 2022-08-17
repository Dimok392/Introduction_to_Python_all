# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.

n = int(input('Введите число n='))
# n = int(input('Введите позицию элемента n='))
a,b=map(int,input('Введите две позиции чисел  через пробел =').split())
proizv=1
my_list=list(range(-n, n+1))
for i in my_list:
    if i==a or i==b : proizv=proizv*my_list[i] 
print(my_list)
print(proizv)

