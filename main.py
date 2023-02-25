from tkinter import *
import random
root = Tk()
root.title("Виселица")
canvas = Canvas(root, width=600, height=600)
canvas.pack()

def but():
    y = 0
    while y < 600:
        x = 0
        while x < 600:
            canvas.create_rectangle(x, y, x + 33, y + 27, fill="white", outline="#999999")
            x = x + 33
        y = y + 27

btn2 = Button(root, text="Выйти из игры", width=15, height=2)
btn2.place(x=258, y=508)
btn2["bg"] = "#00a388"
a = '''Привет игрок, давай поиграем
Пользователь выбирает тему, 
и программа загадывает слово на эту тему.
Игроку известно только количество букв.
Пользователь должен отгадать слово. 
Для этого он вводит поочередно буквы.
Если такой буквы в слове нет, 
то рисуется часть тела человечка,
который может быть повешен в случае,
если игрок не отгадает слово. 
Всего попыток отгадать слово 6. '''
canvas.create_text(320, 235, text=a, fill="black", font=("Helvetica", 14))
fruit = ['апельсин', 'мандарин', 'банан', 'груша', 'яблоко']
def chice(arr):
    but()
    word = random.choice(arr)
    wo = []
    for i in word:
        wo.append(i)
        x = 282
    wor = wo
    wo = list(set(wo))
    list1 = []
    for i in range(1, len(wor) + 1):
        a = canvas.create_text(x, 40, text="_", fill="black", font=("helvetica", "18"))
        x += 33
        list1.append(i)
    alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л",
                "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ",
                "ы", "ь", "э", "ю", "я"]
    er = []
    win = []

    def func(v):
        ind_alf = alphabet.index(v)
        key = alphabet[ind_alf]

        if v in wor:
            ind = wo.index(v)
            b2 = list1[ind]
            wo[ind] = 1
            print(b2)
            def kord():
                x1 = 282
                y1 = 40
                for j in range(1, len(wor) + 1):
                    if b2 != j:
                        x1 += 32
                    else:
                        return x1, y1


            print(kord())

            win.append(v)
            x1, y1 = kord()
            #canvas.create_text(x1, y1, text=wor[ind], fill="black", font=("Helvetica", "18"))
            ind2 = wor.index(v)
            b2 = list1[ind2]
            co = 0
            for j in wor:
                if wor[ind2] == j:
                    co += 1
            if co == 1:
                x1, y1 = kord()
                canvas.create_text(x1, y1, text=wor[ind2], fill="black", font=("Helvetica", "18"))
            else:
                for j in range(len(wor)):
                    print(wor[ind2])
                    print(wor[j])
                    if wor[ind2] == wor[j]:
                        b2 = j + 1
                        x1, y1 = kord()
                        canvas.create_text(x1, y1, text=wor[ind2], fill="black", font=("Helvetica", "18"))

           # print(len(win))
            #print(win)
            #print(len(list1))
            if len(win) == len(wo):
                canvas.create_text(150, 150, text="ВЫИГРАЛ", fill="black", font=("Helvetica", "18"))
                for i in alphabet:
                    btn[i]["state"] = "disabled"
            #canvas.create_text(x1, y1, text=wor[ind], fill="black", font=("Helvetica", "18"))
            btn[key]["bg"] = "green"
            if not v in wo:
                btn[key]["state"] = "disabled"
        else:
            er.append(v)
            btn[key]["bg"] = "red"
            btn[key]["state"] = "disabled"
            if len(er) == 1:
                #golova()
            elif len(er) == 2:
                #telo

    btn = {}

    def gen(u, x, y):
        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: func(u))
        btn[u].place(x=str(x), y=str(y))
    x = 265
    y = 110
    for i in alphabet[0:8]:
        gen(i, x, y)
        x += 33
    x = 265
    y = 136
    for i in alphabet[8:16]:
        gen(i, x, y)
        x += 33
    x = 265
    y = 162
    for i in alphabet[16:24]:
        gen(i, x, y)
        x += 33
    x = 265
    y = 188
    for i in alphabet[24:33]:
        gen(i, x, y)
        x += 33

    def end():
        canvas.create_text(150, 150, text="Проиграл(", fill="black", font=("Helvetica", "18"))
        for i in alphabet:
            btn[i]["state"] = "disabled"






btn1 = Button(root, text="Выбрать тему", width=15, height=2, command = lambda: chice(fruit))
btn1.place(x=258, y=458)
btn1["bg"] = "#00a388"

root.mainloop()