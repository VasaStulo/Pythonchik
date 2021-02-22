a = float(input())
b = float(input())
c = float(input())


def triangle(a, b, c):
    if (a >= b + c) or (b >= a + c) or (c >= a + b):
        res = "Нельзя"
    elif (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) or (c ** 2 == a ** 2 + b ** 2):
        res = "Прямоугольный"
    elif (a ** 2 < b ** 2 + c ** 2) and (b ** 2 < a ** 2 + c ** 2) and (c ** 2 < a ** 2 + b ** 2):
        res = "Остроугольный"
    else:
        res = "Тупоугольный"
    return res


res = triangle(a, b, c)
print(res)
