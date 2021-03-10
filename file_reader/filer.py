path = 'C:/Users/Милый Котенок/PycharmProjects/myFirstProject/Pythonchik/file_reader/'
try:
    xfile = open(path+'macbeth.txt', 'r')
    zfile = open(path+'macbeth-lines.txt', 'w')
except:
    print('File not found!')
    exit()
count = 0
macstart = False
for line in xfile:
    if line.strip().startswith('MACBETH'):
        macstart = True
        count += 1
    elif len(line.strip()) == 0:
        macstart = False
    if macstart:
        zfile.write(line)
print(count)
xfile.close()
zfile.close()