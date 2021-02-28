
k,n = map(int,input().split())
list_car = list(map(int, input().split()))
a_i = 0

for i in range (len(list_car)-1):

    if list_car[i] <= k:
        ostatok = 0
        continue
    elif list_car[i] > k:
        ostatok = list_car[i] - k
        list_car[i] = k
        list_car[i+1] += ostatok
    else:
        ostatok = 0

for i in range(len(list_car)):
    if i == n:
        if k == 0:
            a_i = sum(list_car)
            continue
    elif (list_car[i]) > k:
        a_i = list_car[i] - k
    elif (list_car[i] - k) >= k:
        list_car[i] = k
        a_i = ostatok - list_car[i]
    else:
        a_i = 0

print(a_i)

