from tkinter import *
from tkinter import messagebox
from functools import partial
import random

def ij_to_num(i,j):
    return ((i*3 + j) + 1)

def num_to_ij(num):
    i = (num-1)//3
    j = (num-1)%3
    return(i,j)

def auswerten(liste):
    WinList = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9],[1,5,9], [3,5,7]]
    b = set(liste)
    for testSublist in WinList:
        enth = False
        testSubset = set(testSublist)
        if b >= testSubset:
            enth = True
            for num in testSublist:
                i,j = num_to_ij(num)
                button[i][j].config(bg= "red")
            break
    return (enth)

def comp_setzen():
    if not freie_felder:
        Message("UNENTSCHIEDEN")
    else:
        n = random.choice(freie_felder)
        freie_felder.remove(n)
        o_felder.append(n)
        i, j = num_to_ij(n)
        button[i][j].config(text="O")
        if auswerten(o_felder):
            Message("OH NO - Computer hat gewonnen")

def button_action(i, j):
    n = ij_to_num(i,j)
    if n in freie_felder:
        freie_felder.remove(n)
        x_felder.append(n)
        button[i][j].config(text = "X")
        if auswerten(x_felder):
            Message("YES - Du hast gewonnen")
        else:
            comp_setzen()
    else:
        messagebox.showinfo(message="Feld ist schon belegt")

def Neustart():
    global freie_felder
    freie_felder = list([i for i in range(1,10)])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in freie_felder:
        i, j = num_to_ij(num)
        button[i][j].config(text="",bg = "SystemButtonFace")
    del x_felder[:]
    del o_felder[:]

def Message(text):
    MsgBox = messagebox.askquestion (text,'Nochmal spielen?')
    if MsgBox == 'no':
       master.destroy()
    else:
        Neustart()

def play():
    global button
    global freie_felder
    global x_felder
    global o_felder
    global master

    master = Tk()
    master.title("Tic Tac Toe (@Griessemer)")

#Erstellen des Spielfeldes:
    l1 = Label(master, text="Player 1 ist X / Computer ist O")
    l1.grid(row=0, column=0, columnspan = 3, pady=10)
    l2 = Label(master, text="Bitte Feld auswählen Player 1 oder")
    l2.grid(row=1, column=0, columnspan = 3, pady=10)
    b_comp = Button(master, text = "Computer soll beginnen", bg = "lightgreen", command=comp_setzen)
    b_comp.grid(row=2, column=0, columnspan = 3, padx=15, pady=15)

    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            b_comand = partial(button_action, i, j)
            button[i][j] = Button(
                    master, bd=5, command=b_comand, height=8, width=16)
            button[i][j].grid(row=m, column=n)

    b_exit = Button(master, text = "QUIT", bg = "red", font=("Times", 20), command=master.destroy)
    b_exit.grid(row=6, column=0, columnspan = 3, padx=15, pady=15)
#

    freie_felder = list([i for i in range(1,10)])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x_felder = []
    o_felder = []

    mainloop()

if __name__ == '__main__':
    play()
