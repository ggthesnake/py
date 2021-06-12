def personal_inf(**kwargs):
    return ' '.join(kwargs.values())


name = input('Введите имя ')
surname = input('Введите фамилию ')
birthday = input('Введите дату рождения ')
city = input('Введите город ')
email = input('Введите почту ')
phone = input('Введите телефон ')

print(personal_inf(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))
