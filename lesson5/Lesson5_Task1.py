f1 = open("my_file.txt", 'w')

while True:
    user_input_data_string = str(input("напишите Ну И Пусть в разных строках:  "))
    if user_input_data_string != '':
        f1.write(user_input_data_string + '\n')
        continue
    else:
        print('Мячи сложили, сели.')
        f1.flush()
        break
f2 = open("my_file.txt", 'r')
content = f2.read()
print(content + 'будет нелегким мой пу-у-уть')

f1.close()
