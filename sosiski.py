# k, n = map(int,input().split())
a = list()
# for i in range(k):
#          a.append(list(map(int, input().split())))
a = [[0,5], [13,18], [25,475]]
sum = 0
for i in range(len(a)):
    for j in range(len(a[i])-1):
        sum += ((a[i][j+1]-a[i][j])+1)
        print(sum)
print(sum)