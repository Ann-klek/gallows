from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("300x250")

canvas = Canvas(bg="white", width=250, height=200)
canvas.pack(anchor=CENTER, expand=1)




btimg = PhotoImage(file="red-cross-mark-clipart-227244.png")
btimg = btimg.subsample(10, 10)
#btn = Button(text="", width=100, image=btimg, bd=0,  highlightthickness=0).place(x=133,y=100)
#btnId = canvas.create_window(10, 20, anchor=NW, window=btn, width=100, height=50)

btn04 = Button(text="", width=100, image=btimg, bd=0, highlightthickness=0).place(x=133, y=100)
btn04Id = canvas.create_window(10, 20, anchor=NW, window=btn04, width=100, height=50)
root.mainloop()