revenue = float(input('Внесите значение выручки - '))
costs = float(input('Внесите значение издержек - '))
result = revenue - costs
if result > 0:
    print(f'Поздравляем, ваша компания работает с прибылью {result}')
    print(f'Рентабельность выручки -  {result / revenue: .3f}')
    staff = int(input('Введите количество сотрудников - '))
    print(f'Прибыль на одного сотрудника - {result / staff:.3f}')
elif result < 0:
    print(f'Ваша фирма работает с убытком - {result}')
else:
    print(f'Ваша фирма работает без убытка, но и прибыли нет')
