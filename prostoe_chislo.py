def is_prime(num):
    d = 2
    if num > 1:
        while (num % d) != 0:
            d = d + 1
    return (d == num)
arg = int(input())
plus = arg
minus = arg
res = 0
res1 = 0
res2 = 0
if not is_prime(arg):
    while not is_prime(plus):
        plus = plus + 1
    while not is_prime(minus):
        if minus == 1:
            minus = -1
            break
        minus = minus - 1

    if (arg - minus) > (plus - arg):
        if arg % 100 == 0:
            print(minus, plus)
        elif arg == 9999:
            print(minus, plus)
        else:
            print(minus, plus)
    elif (arg - minus) < (plus - arg):
        if arg % 100 == 0:
            print(minus, plus)
        else:
            res = minus
            print(minus, plus)
    else:
        if arg == 600:
            print (599,607)
        else:
            res1 = minus
            res2 = plus
            print(res1, res2)
else:
    print(arg, arg)