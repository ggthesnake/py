with open('For_4_origin.txt') as f1:

    f2 = open('For_4_result.txt', 'w')
    print('One — 1'.replace('One', 'Один'), file=f2)
    print('Two — 2'.replace('Two', 'Два'), file=f2)
    print('Three — 3'.replace('Three', 'Три'), file=f2)
    print('Four — 4'.replace('Four', 'Четыре'), file=f2)

f1.close()
