# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
my_list = [1.1, 1.2, 3.1, 5, 10.01]
my_rez_razn = []
for i in range((len(my_list))):
    my_rez_razn.append ((my_list[i])%1)
print(my_rez_razn)
min = my_rez_razn[0]
max = my_rez_razn[0]
for i in range((len(my_rez_razn)-1)):
    if my_rez_razn[i+1] >max:
        max = my_rez_razn[i+1] 
    else:
        min=my_rez_razn[i+1]
print(f'разница между максимальной и минимальноq частью после запятой = {round(max-min,3)}') 

