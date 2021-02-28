#Задана последовательность идентификаторов, разделенных одним или несколькими пробелами.
#Найти и напечатать все идентификаторы, не содержащие цифр.
lst = input().strip().split()
string = ''
for i in range(len(lst)):
    if not(any(map(str.isdigit, lst[i]))):
        string+=(lst[i].strip()+' ')
string = string[:-1]
print(string)

