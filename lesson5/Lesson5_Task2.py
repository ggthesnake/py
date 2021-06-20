

f1 = open("lermontov.txt", 'r', encoding='utf-8')
# print(f1.read())
# f1.seek(0)
lines = 0
wordsinline = 0
for line in f1:
    lines += 1
    wordsinline = len(line.split())
    print(f'{" ".join(line.split())}' + ' - Это строка номер ' + str(lines) + ', в ней ' + str(wordsinline) + ' слов.')
print('Всего строк: ' + str(lines))

kolvo_strok = sum(1 for line in open('lermontov.txt'))
print('количество строк:', sum(1 for line in open('lermontov.txt')))

while True:
    line = f1.readline()

    if not line:
        break
    print(line.strip(), ' <-||simbols in line:', len(line))





# f1.seek(0)
#s = f1.readline()
#letters_inline = len(s)
print('колво букв:', len(f1.readline()))
# f1.seek(letters_inline+2)
s = f1.readline()
letters_inline = len(s)
print('количество строк:', kolvo_strok, 'колво букв:', letters_inline)
s = f1.readline()
letters_inline = len(s)
print('количество строк:', kolvo_strok, 'колво букв:', letters_inline)
s = f1.readline()
letters_inline = len(s)
print('количество строк:', kolvo_strok, 'колво букв:', letters_inline)
s = f1.readline()
letters_inline = len(s)
print('количество строк:', kolvo_strok, 'колво букв:', letters_inline)


f1.close()
