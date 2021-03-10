path = '/4 kontest/'
xfile = open(path+'input.txt', 'r')
zfile = open(path+'output.txt', 'w')

def initilizeDictionary(inputStr):
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    d = dict.fromkeys(inputStr)
    i = 0
    for key, value in d.items():
        d[key] = arr[i]
        i += 1
    return d

def decrypt(d, str):
    string = ""
    for iter in str:
        if not iter.isalpha():
            string += iter
        else:
            for key, value in d.items():
                if iter.lower() == value.lower():
                    if iter.isupper():
                        string += key.upper()
                    else:
                        string += key
    return string

for line in xfile:
    d = initilizeDictionary(line.strip())
    break

for line in xfile:
    decryptionLine = decrypt(d, line)
    zfile.write(decryptionLine)

xfile.close()
zfile.close()