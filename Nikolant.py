def calc():
    pi = 3
    dev = 2
    accuracy = 5000

    for i in range(accuracy):
        pi += (4 / (dev * (dev + 1) * (dev + 2))) * pow(-1, i)
        dev += 2

    print(pi)


if __name__ == "__main__":
    calc()
