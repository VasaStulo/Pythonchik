from array import *

#На вход программе подается N элементов (1<=N<1000).
#Элементы могут принимать целые значения от -10 000 до 10 000 включительно.
#Напишите программу, позволяющую найти и вывести количество пар элементов,
# в которых хотя бы одно число делится на 7.
#В данной задаче под парой подразумевается два подряд идущих элемента.

n = int(input())
count = 0
a = []

for i in range(0, n):
    a.append(int(input()))

for i in range(0, n-1):
    if (a[i] % 7 == 0 or a[i+1] % 7 ==0):
       count += 1

print(count)
print(a)


