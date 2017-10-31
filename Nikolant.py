PI = 3
dev = 2
accurancy = 5000

for i in range(accurancy):
    PI += (4 / (dev * (dev + 1) * (dev + 2))) * pow(-1, i)
    dev += 2

print(PI)
