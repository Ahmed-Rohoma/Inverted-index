def low(z):
    return z.lower()

def first(z):
    return z[0]

def squish(x):
    s = set(x)
    return sorted([(i,x.count(i)) for i in s],key = first)

def clean(x):
    y = ""
    s = [".",",","-","?"]
    for i in x:
        if i in s:
            continue
        y += i
    return y

d = {}
ln = 0

for line in open('test.txt') :
    print(line)
    ln += 1
    line = clean(line)
    line = line.split()
    for word in line :
        if word not in d :
            d[word] = []
            d[word].append(1)
            d[word].append([ln])
        else :
            d[word][0] += 1 
            d[word][1].append(ln)
print('list of D ')
list_D = list(d)
list_D.sort(key = low)
for k in list_D :
    print(k, d[k][0], squish(d[k][1]))

            

