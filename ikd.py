crypt = {"a":"c", "t":"g", "g":"a", "c":"t"}
s = (tgtacg)
r = ""
for i in range(len(s)):
    for k, v in crypt.items():
        if v == s[i]:
            r += k
print(r)