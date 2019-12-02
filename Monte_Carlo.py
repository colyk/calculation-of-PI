import random


def check(x, y, r):
    if (x ** 2 + y ** 2) <= r ** 2:
        return 1
    return 0


def calc_pi(r=1, points=10000):
    sum_ = 0
    for i in range(points):
        random.seed()
        x = random.uniform(0, r)
        y = random.uniform(0, r)
        if check(x, y, r):
            sum_ += 1
    return sum_ / points * 4


def calc():
    r = 1000000
    points = 100000
    pi = 0
    for i in range(1, 100):
        a = str(calc_pi(r, points))[:6]
        if a == '3.1415':
            print('Found ', i)
            break
        pi += float(a)

    print(pi / i)


if __name__ == '__main__':
    calc()
