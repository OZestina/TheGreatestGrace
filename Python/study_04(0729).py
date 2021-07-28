from tkinter import *
from tkinter import messagebox

def login():
    id2 = id_entry.get()
    print(id2)
    if id2 == 'root':
        messagebox.showinfo("succeeded", "congrats")
        print("login")

        result = messagebox.askquestion("ok?","really?")
        print(result)
        if result == "yes":
            print("OK")
        else:
            print("Then no!")

    else:
        messagebox.showinfo("failed", "try again")
        print("login failed")
w=Tk()
w.geometry("500x250")

id = Label(w, text='id입력',font=('궁서',30))
id.pack()
id_entry = Entry(w,font=('궁서',30), bg='blue',fg='white')
id_entry.pack()

b = Button(w,
           text = '로그인처리',
           font=('궁서',30),
           bg='yellow',
           command=login
           )
b.pack()
w.mainloop()

import datetime
now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

import calendar
print(calendar.month(now.year, now.month))

dic = {1:'apple',2:'banana'}
for x in dic:
    print(x)    #key만 찍힘
