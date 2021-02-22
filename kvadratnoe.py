import math

try:
    a = float(input())
    b = float(input())
    c = float(input())

    discr = b ** 2 - 4 * a * c

    if discr > 0 and a == 0:
        print('%.3f' % (-c/b))

    elif discr == 0:
        x1 = -b / (2 * a)
        x2 = x1
        print('%.3f' % x1, '%.3f' % x2)

    else:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print('%.3f' % x1, '%.3f' % x2)

except:
    print("ERROR")
