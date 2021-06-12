def sum_num():
    s = 0
    while True:
        in_list = input('Введите число или Q для выхода: ').split()
        for num in in_list:
            if num == 'q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print('Нажмите q для выхода - ')
        print(f'Сумма чисел = {s}')


print(sum_num())
