# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
x = int(input('Введите 0 либо 1 x='))
y = int(input('Введите 0 либо 1 y='))
z = int(input('Введите 0 либо 1 z='))
b = not(x or y or z)
print(f'b={b}')
c = not x and not y and not z
print(f'c={c}')
if b == c:
    print(True)
else:
    print(False)


# x∨¬y∨z
# 0	0	0	 1	     1 	0	0	  1
# 0	0	1	 1	     1 	0	1	  1
# 0	1	0	 0	     1	1   0	  1
# 0	1	1	 1	     1	1	1	  1
# ¬(X ⋁ Y ⋁ Z) =x∨¬y∨z для проверки
# if not(x and y and z) == x and (not y)and z


# ¬(X ⋁ Y ⋁ Z)                                                        ¬X ⋀ ¬Y ⋀ ¬Z
# 0	 0	0	 1	   1  0	 0	 0                                 0  0	 0	    1	       1  0  0	     0
# 0	 0	1	 0	   1  0	 1	 0                                 0  0	 1	    0	       1  0	 1	     0
# 0	 1	0	 0	   1  1	 0	 0                                 0  1	 0	    0	       1  1	 0	     0
# 0  1	1	 0	   1  1	 1	 0                                 0  1	 1	    0	       1  1	 1	     0
