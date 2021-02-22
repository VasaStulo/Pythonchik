#Компания мальчиков нарвала в саду яблок.
# Они хотят разделить яблоки между собой поровну, а то что останется, отдать маме на пирог.
#Определите, сколько яблок достанется каждому из них, а сколько они отдадут маме.
a = input()
b = input()
number_boys = int(a)
number_apple = int(b)


def division(number_boys, number_apple):
    finish_apple_mum = 0
    if (number_apple % number_boys) > 0:
        finish_apple_mum = number_apple % number_boys
        finish_apple_boys = number_apple // number_boys
    elif number_boys > number_apple:
        finish_apple_boys = 0
        finish_apple_mum = number_apple
    else:
        finish_apple_boys = number_apple // number_boys
    return finish_apple_boys, finish_apple_mum

z,y = division(number_boys,number_apple)
print(z,y)

