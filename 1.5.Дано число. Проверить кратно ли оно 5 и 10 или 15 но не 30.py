# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
n = int(input('Введите сило n='))
if (n%5==0 or n%10==0 or n%15==0) and (n%30!=0):
    print(n)
else:
    print('не удовлетворяет условиям')