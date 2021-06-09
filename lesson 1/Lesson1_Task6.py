while True:
    days = 5
    start_km = float(input('Результат вначале -'))
    final_km = float(input('Результат на финише - '))
    if start_km <= 0 or final_km < 0:
        print ('Результат должен быть больше 0, старт больше или равен 0')
    else:
        while start_km < final_km:
            start_km *= 1.1
            days += 1
            print(f'Спортсмен достигнет результата за {days}дней')
