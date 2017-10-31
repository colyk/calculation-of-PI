PI = 0
dev = 1
accurancy = 50000 # Ошибка

for i in range(accurancy):
    PI += (4 / dev) * pow(-1, i)
    dev += 2

print(PI)
