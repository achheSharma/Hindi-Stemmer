import codecs

filename = "test_dataset.txt"
with codecs.open(filename, encoding='utf-8') as f:
    txt = f.read()
f.close()
file = open("out.txt",'w', encoding='utf-8')

''' testing '''
# file_maatra = open("maatra.txt",'w', encoding='utf-8')
# file_temp = open("temp.txt", 'w', encoding = 'utf-8')
# print(len(txt))

maatra = ["ि", "ा", "ी", "े", "ु", "ू", "ँ", "ं", "ो", "ि◌या", "ि◌यो", "◌ाए"]

''' Stemming '''
len_of_word = 0
bytes_read = 0
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
    for k in maatra:
        if a.rfind(k)!=-1:
            if(len(a.split(k)[0])!=1):
                stems.append(a.split(k)[0])
    if (txt[i] == '\n'):
        i = i+1
sets=set(stems)
