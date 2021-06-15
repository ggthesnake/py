from itertools import count, cycle

print('Нажмите Enter для геренации ',
      ' для выхода нажмите q')
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('Нажмите Enter для следующего повтора, для выхода',
      ' из программы нажмите q')
u_list = input('Введите список, с пробелом между элементами: ').split()
iter_ = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter_), end='')
    quit = input()