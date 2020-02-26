word_dict = set()
f = open("Oxford English Dictionary.txt", 'r')

for line in f:
    tline = line.rstrip('\n').upper()
    # print(line)
    # print(tline)
    tline = tline.split(" ")
    tword = tline[0]
    # print(tword)

    if tword != "":
        if tword[len(tword)-1].isnumeric():
            tword = tword[0:len(tword)-1]
        if tword.isalpha() and len(tword) > 1:
            word_dict.add(tword)

 
f.close()
print("********")
sort_dict = sorted(word_dict)
count = 0
outF = open("oed.txt", "w")
for tword in sort_dict:
    count += 1                
    print(tword)
    outF.write(tword + '\n')
    # if count > 20:
    #     break
print(count)
print(len(sort_dict))
outF.close()
