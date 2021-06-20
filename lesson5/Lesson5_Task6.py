d = {}
with open('lessons.txt', encoding='utf-8') as f1:
    for line in f1:
        name, stats = line.split(':')
        elems = [i for i in stats if i == ' ' or (i >= '0' and i <= '9')]
        name_sum = sum(map(int, "".join(elems).split()))
        d[name] = name_sum
print(d)