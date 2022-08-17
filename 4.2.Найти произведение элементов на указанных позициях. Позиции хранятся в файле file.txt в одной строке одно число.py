#Задать список из N элементов, заполненных числами из [-N, N].
#Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число


# list_of_numbers=[-3, -2, -1, 0, 1, 2, 3]
# file = open('text.txt', "r")
# data = file.read()
# list_of_rows = data.split()
# file.close()
# print(f"{list_of_rows}")
# result = 1
# for i in list_of_rows:
#     result *= list_of_numbers[int(i)]

# print(f"{list_of_numbers} -> {list_of_rows} -> {result}")
with open('test.txt', 'w') as file:
    indices = input('Введите числа через пробел')
    indices = indices.split(' ')
    for el in indices:
        file.write(f'{el}\n')

list_of_nums = [-3, -2, -1, 0, 1, 2, 3]

with open('test.txt', 'r') as file:
    a = file.read()
list_of_indices = a.split()
list_of_indices = list(map(int, list_of_indices))

res = 1
for el in list_of_indices:
    if el < len(list_of_nums):
        res *= list_of_nums[el]
print(res)