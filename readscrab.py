import mysql.connector
hostname = 'localhost'
username = 'root'
password = 'cassword'
database = 'wordgen'
# word_dict = {}
# word_dict[tword] = {'pscore': 0, 'nscore': 0, 'def': tdef}

cnx = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database)
cursor = cnx.cursor()

f = open("scrabdef.txt", 'r')
count = 0

for line in f:
    tline = line.rstrip('\n')
    tword, tdef = tline.split("\t")

    add_word= ("INSERT INTO wordlist "
               "(word, pscore, nscore, definition) "
               "VALUES (%s, %s, %s, %s)")
    data_word = (tword, 0, 0, tdef)
    cursor.execute(add_word, data_word)
    count +=1 
    # if count > 20:
    #     break

f.close()
cnx.commit()
cursor.close()
cnx.close()

# print(count)
# print(len(word_dict))
# print("********")
# sort_dict = sorted(word_dict)
# count = 0
# # outF = open("sd.txt", "w")
# print(word_dict['AARDVARK'])
# print(type(word_dict))
# print(type(sort_dict))
# for k, v in word_dict.items():
#     print(k, v)
#     count += 1                
#     if count > 20:
#         break
# # for tword in sort_dict:
#     print(tword)
#     outF.write(tword + '\n')

# print(count)
# print(len(sort_dict))
# outF.close()
