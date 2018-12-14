import random


def check(x, y, r):
    if x**2 + y**2 <= r**2:
        return 1
    return 0


def calc_PI(R=1, points=10000):
    sum_ = 0
    for i in range(points):
        random.seed()
        x = random.uniform(0, R)
        y = random.uniform(0, R)
        if check(x, y, R):
            sum_ += 1
    return sum_ / points * 4


if __name__ == '__main__':
    R = 1000000
    points = 100000
    PI = 0
    for i in range(1, 10):
        a = str(calc_PI(R, points))[:6]
        if a == '3.1415':
            print('Found ', i)
            break
        PI += float(a)

    print(PI/i)
