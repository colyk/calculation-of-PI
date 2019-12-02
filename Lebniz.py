def calc():
    pi = 0
    dev = 1
    accuracy = 50000

    for i in range(accuracy):
        pi += (4 / dev) * pow(-1, i)
        dev += 2

    print(pi)


if __name__ == "__main__":
    calc()
