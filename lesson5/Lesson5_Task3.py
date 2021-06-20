# -*- coding: utf-8 -*-
d = {}
with open("zp.txt", encoding='utf-8') as file:
    for line in file:
        key, value = line.split()
        d[key] = int(value)
#    print(d.keys())
for k, v in d.items():
    if int(v) < 20000:
        print('У ' + k +'а ЗП меньше МРОТ :(')
midl = sum(d.values())/len(d)
print('Средняя ЗП = '+ str(midl) + ' руб.')

file.close()
