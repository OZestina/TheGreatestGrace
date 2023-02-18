import tkinter as tk

no_times = 0

def happily_ever_after():
    global no_times
    button_yes.destroy()
    button_no.destroy()
    label.config(text='I ❤ U')
    if no_times != 0:
        sub_label.config(text='(even though you clicked no ' + str(no_times) + ' times...)')

def change_text():
    global no_times
    no_times += 1
    if no_times == 2:
        button_no.place(x=180, y=170)
    if no_times == 3:
        button_yes.config(width=27)
        button_no.place(x=280, y=170)
    if no_times == 4:
        button_yes.config(width=10)
        button_no.place(x=50, y=120)
        button_yes.place(x=180, y=120)
    if no_times == 5:
        label.config(text='WILL U BE MY VALENTINE?', foreground='red')
        button_yes.place(x=50, y=120)
        button_no.place(x=180, y=120)
    if no_times == 6:
        label.config(text=":/", foreground='black', font=('Arial', 20))
    if no_times == 7:
        label.config(text=":'(", foreground='red')
    if no_times == 8:
        window.config(background='black')
        sub_label.config(background='black')
        label.config(text="FXCK U '^'", foreground='red', background='black', font=('Arial', 30))
        button_yes.destroy()
        button_no.destroy()


window = tk.Tk()
window.title("Hello, it's me :)")
window.geometry("300x190")

label = tk.Label(window, text='Will you be my Valentine?', font=('Arial', 15), height=3)
sub_label = tk.Label(window, font=('Arial', 12), foreground='grey')
label.pack()
sub_label.pack()

button_yes = tk.Button(window, text='YES', command=happily_ever_after, width=10, height=2)
button_no = tk.Button(window, text='no', command=change_text, width=10, height=2)
button_yes.place(x=50, y=120)
button_no.place(x=180, y=120)

window.mainloop()