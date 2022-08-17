# Дан список чисел. Создать список в который попадают числа,
# описывающие возрастающую последовательность и 
# содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# list_input = [5, 2, 3, 4, 6, 1, 7]
# def max_in_list(list_of_numbers):
#     max = list_of_numbers[0]
#     for i in list_of_numbers:
#         if i > max:
#              max = i
#     return max
# new_list_dic = {}

# index = 0
# list_input = [5, 2, 3, 4, 6, 1, 7]
# for n in range(1,len(list_input)):
#     for i,item in enumerate(list_input[:-n]):
#         new_list = [list_input[i]]
#         for j,item_2 in enumerate(list_input[i+n:]):
#             if item_2 > max_in_list(new_list):
#                 new_list.append(item_2)


# if new_list not in new_list_dic.values():
#     new_list_dic[index] = new_list
# index += 1

# for i in new_list_dic:
#     print(f"{i} : \t{new_list_dic[i]}")
l = [1, 5, 2, 3, 4, 6, 1, 7]

r1=[]
for j in range(0,len(l)):
    for i in range(j,len(l)):
        if i ==j:
            r1.append(l[i])
        elif l[i]>r1[-1]:
            r1.append(l[i])
    print(r1)
    r1.clear()