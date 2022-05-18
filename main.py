def low(char):
    return char.lower()

def first(char):
    return char[0]

def squish(x):
    s = set(x)
    return sorted([(i,x.count(i)) for i in s],key = first)

def clean(line):
    new_line = ""
    removed_char = [".",",","-","?"]
    for char in line:
        if char in removed_char:
            continue
        new_line += char
    return new_line

data = {}
length = 0

for line in open('data.txt') :
    length += 1
    line = clean(line)                  # remove useless characters
    line = line.split()                 
    for word in line :
        if word not in data :              # if exist create new field
            data[word] = []
            data[word].append(1)
            data[word].append([length])
        else :                          # if not exist add 1 to counter
            data[word][0] += 1 
            data[word][1].append(length)       

list_of_Data = list(data)
list_of_Data.sort(key = low)
for k in list_of_Data :
    print(k, data[k][0], squish(data[k][1]))

            

