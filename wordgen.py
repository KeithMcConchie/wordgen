import tkinter as tk
import itertools as it
import mysql.connector
hostname = 'localhost'
username = 'root'
password = 'cassword'
database = 'wordgen'

dict_min_word_length = 3
dict_max_word_length = 7
min_word_length = 3
max_word_length = 7
# word_dict = set()
word_dict = {}
l = []

def generate_word_list(g_letter_str, l):                        
    l.clear()
    for i in range(3,8):
        l.append([])
    print(l)
    game_letters = list(g_letter_str)
    game_letters.sort()
    print (game_letters)
    count = 0


    for i in range(min_word_length, len(game_letters)+ 1):
        # print(i)
        p = set(it.permutations(game_letters, i))
        for a in p:
            t_word = "".join(a)
            if t_word in word_dict: 
                count += 1
                # print(t_word)
                l[i-3].append(t_word)

        l[i-3].sort()


def load_dictionary():
    cnx = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database)
    cursor = cnx.cursor()
    
    query = ("SELECT word, pscore, nscore, definition FROM wordlist ")
    cursor.execute(query)
    
    count = 0
    for (word, pscore, nscore, definition) in cursor:
        if dict_min_word_length <= len(word) <= dict_max_word_length:
            count += 1
            # word_dict.add(word)
            word_dict[word] = {'pscore': pscore, 'nscore': nscore, 'definition': definition}
    cursor.close()
    cnx.close()

# def load_dictionary():
#     f = open("scrabble.txt", 'r')
#     count = 0
#     for line in f:
#         tline = line.rstrip('\n').upper()
#         if tline.isalpha():
#             if dict_min_word_length <= len(tline) <= dict_max_word_length:
#                 count += 1
#                 word_dict.add(tline)
#     f.close()

# def load_dictionary_wdefs():
#     f = open("scrabdef.txt", 'r')
#     count = 0
#     for line in f:
#         tline = line.rstrip('\n').upper()
#         if tline.isalpha():
#             if dict_min_word_length <= len(tline) <= dict_max_word_length:
#                 count += 1
#                 word_dict.add(tline)
#     f.close()


def get_letter_string():
    g_letter_str = e.get()
    w.configure(text=g_letter_str)
    generate_word_list(g_letter_str, l)
    load_listbox()

def onselect(evt):
    # definition = listbox.get(tk.ACTIVE)
    # def_label.configure(text=definition)
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    definition = word_dict[value]['definition']
    # def_label.configure(text=value)
    def_label.configure(text=definition)
    print('You selected item %d: "%s"' % (index, value))


def load_listbox():
    listbox.delete(0, tk.END)
    for i in range(min_word_length, max_word_length + 1):
        for t_word in l[i-3]:
            listbox.insert(tk.END, t_word)

load_dictionary()
g_letter_str = "JOURNEY"

win = tk.Tk()
e = tk.Entry(win)
e.pack()
e.focus_set()
w = tk.Label(win, text="foo")
w.pack()
b = tk.Button(win, text="get", width=10, command=get_letter_string)
b.pack()
listbox = tk.Listbox(win)
# listbox.config(font="Arial")
listbox.pack()
def_label = tk.Label(win, text="Definition place holder")
def_label.pack()

listbox.bind('<<ListboxSelect>>', onselect)
win.geometry("800x480")
win.config(bg="blue")
win.mainloop()
# this changes the background colour of the 2nd item
    # listbox.itemconfig(1, {'bg':'red'})

print(l)