# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
with open ('file_test.txt','w',encoding='utf8') as file:
    file.write(input('Введите последовательность ' ''))
with open('file_test.txt', 'r') as file:
    my_list = list(map(int, file.read().split()))
print(f'Начальный список{my_list}')
for i in range(1,len(my_list)):
    if my_list[i]-1 != my_list[i-1]:
        print(f'Недостающие элемент {my_list[i-1]+1}')
