import codecs

filename = "test_dataset.txt"
with codecs.open(filename, encoding='utf-8') as f:
    txt = f.read()
f.close()
file = open("output.txt",'w', encoding='utf-8')

maatra = ["ि", "ा", "ी", "े", "ु", "ू", "ँ", "ं", "ो", "ि◌या", "ि◌यो", "◌ाए"]

''' Stemming '''
to_remove = ['\ufeff', '\r']
i=0
stems=[]
while(i<len(txt)):
    a = []
    while(txt[i]!='\n'):
        a.append(txt[i])
        i=i+1
    a = [k for k in a if k not in to_remove]
    a= ''.join(a)
    b = a
    file.write(b + " : ")
    k = 0
    while(k<len(maatra)):
        x = a.rfind(maatra[k])
        k = k+1
        if x == len(a)-1:
            a = a[:x]
            k = 0
    file.write(a)
    file.write("\n")
    if (txt[i] == '\n'):
        i = i+1
file.close()
