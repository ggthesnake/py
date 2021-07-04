second = int (input("Введите кол-во секунд - "))
hour = int (second // 3600)
second %= 3600
minute = int (second // 60)
second %= 60


print (hour, + minute, + second)
