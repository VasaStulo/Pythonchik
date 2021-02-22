numb = int(input())
numb_two = 1
max = 0
sum = 0
while numb_two <= numb:

    if numb % numb_two == 0 :
        max = numb_two
        numb_two += 1
    else:
        numb_two += 1



