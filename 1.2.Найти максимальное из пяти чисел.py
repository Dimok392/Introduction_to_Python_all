#Найти максимальное из пяти чисел
# print('Введите первое чило a')
# a = int(input())
# print('Введите второе чило b')
# b = int(input())
# print('Введите третье чило с')
# c = int(input())
# print('Введите четвёртое чило d')
# d = int(input())
# print('Введите пятое чило е')
# e = int(input())
# max = 0
# if(a>max): max=a
# if(b>max): max=b
# if(c>max): max=c
# if(d>max): max=d
# if(e>max): max=e
# print (max)
# for i in [b,c,d,e]:
#     if max < i: max=i
# print (max)
for i in range (1,6):
    a=int(input(f'Введите число {i} = '))
    if i==1: max=a
    elif max<a: max = a
print (max)