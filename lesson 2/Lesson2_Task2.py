a = input('Введите значения с пробелами: ').split()
i = 0
print(f'Оригинальный список {a}')
while i + 1 < len(a):
     if i % 2 == 0:
         a.insert(i, a.pop(i + 1))
     i += 1
print(f'Измененный список {a}')