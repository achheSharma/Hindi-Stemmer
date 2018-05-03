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

maatra = ["ि", "ा", "ी", "े", "ु", "ू", "ँ", "ं", "ो"]

''' Copy test_dataset to testing_dataset to avoid unwanted'''
fileout = open("testing_dataset.txt", 'w', encoding = 'utf-8')
for i in range(len(txt)):
    fileout.write(txt[i])
with codecs.open("testing_dataset.txt", encoding='utf-8') as f:
    txt = f.read()
# print(len(txt))

''' Stemming '''
len_of_word = 0
bytes_read = 0
for i in range(0,len(txt)):
    j = 0
    # file_temp.write("txt[" + str(i) +"] : " + txt[i] + "\n")
    if txt[i] == "\n":
        len_of_word = len_of_word-1
        # print("bytes_read : ", i)
        # print("len_of_word : ", len_of_word)
        # for j in range(i-2, (i-2)-len_of_word, -1):
        #     file_maatra.write("txt[" + str(j) +"] : " + txt[j] + "\n")
        for j in range(i-2, (i-2)-len_of_word, -1):
            if txt[j] not in maatra:
                break
        # print(j)
        for k in range((i-2)-len_of_word+1, j+1):
            file.write(txt[k])
        file.write("\n")
        len_of_word = 0
    else:
        len_of_word = len_of_word+1

