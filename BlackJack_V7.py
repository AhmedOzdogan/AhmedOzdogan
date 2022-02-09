# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 19:43:55 2022

@author: ahmed



restart butonu kapatılacak
kodlar kontrol edilip sadeleştirilecek
"""

from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import random
import sys
import os


root = Tk()
root.title("BlackJack")
root.geometry("1000x1000")


root.attributes("-topmost", True)


menu_ = Menu(root)
root.config(menu = menu_)
menu_sub = Menu(menu_, tearoff = 0)
menu_.add_cascade(label="File", menu=menu_sub)
menu_sub.add_command(label = "Exit", command=root.destroy)



font_1 = "Ariel 20"
w = 60
w1 = 130
h = 1
h1 = 200
cs = 10
money = 10000

moneystr = str(money)+ "$"

img = (Image.open("BlackjackHeader.jpg"))
resized_image = img.resize((200,150), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image, master = root)
header = Label(root, image = new_image).grid(row = 0, column = 0,columnspan=cs)


    
def dealerCards():
    global labelCard
    for x in range(len(dealerHand)):
        labelCard = Label(root,
                          justify = CENTER,
                          image = dealerHand[x])
        labelCard.grid(row = 5,column = x)

def giveCard():
    global labelCard_3
    global cs
    pickCard(1,125,181,yourHand,yourResult)
    num = len(yourHand)
    labelCard_3 = Label(root,
                      justify = CENTER,
                      image = yourHand[num-1])
    labelCard_3.grid(row = 2,column = num-1)
    result()
    checker()


def stand():
    global stop
    stop = True
    while sum(dealerResult) <17:
        
        pickCard(1,125,181,dealerHand,dealerResult)
        
        if sum(dealerResult) >21 and  11 in dealerResult:
                
                for x in range(len(dealerResult)):
                    if dealerResult[x] == 11:
                        dealerResult[x] = 1
                        break
    num = len(dealerHand)
    card_1.destroy()
    card_2.destroy()
    dealerCards()
    result()
    checker()
    button_1['state'] = DISABLED
    button_2['state'] = DISABLED

    
    
def restart():

    global yourHand,yourResult,dealerHand,dealerResult,card_1,card_2,stop,win,lose,stop

    stop = False
    win = False
    lose = False
    
    yourHand = []
    yourResult = []
    dealerHand = []
    dealerResult = []
    try :
        labelCard.configure(image = "")
    except :
        pass
    try :
        labelCard_2.configure(image = "")
    except :
        pass
    try :
        labelCard_3.configure(image = "")
    except :
        pass
    try:
        card_1.destroy()
        card_1 = Label(root,
                  justify = CENTER)

        card_1.grid(row = 5,column = 0)

    except:
        pass
    try:
        card_2.destroy()
        card_2 = Label(root,
                  justify = CENTER)

        card_2.grid(row = 5,column = 1)
    except:
        pass
    try:
        start()

    except:
        pass
    result_label.configure(text = "")
    button_1['state'] = NORMAL
    button_2['state'] = NORMAL
    stop = False



label_yh = Label(root,
                text= "Your Hand",
                font = font_1,
                justify=CENTER,
                width = w,
                height = h).grid(row = 1, column = 0,columnspan=cs)

label_yr = Label(root,
                font = font_1,
                text = "text",
                justify=CENTER,
                width = w,
                height = h)

label_yr.grid(row = 3, column = 0,columnspan=cs)


label_dh = Label(root,
                text= "Dealers Hand",
                font = font_1,
                justify=LEFT,
                width = w,
                height = h).grid(row = 4, column = 0,columnspan=cs)

card_1 = Label(root,
                  justify = CENTER)

card_1.grid(row = 5,column = 0)

card_2 = Label(root,
                  justify = CENTER)

card_2.grid(row = 5,column = 1)

label_dr = Label(root,
                font = font_1,
                justify=LEFT,
                width = w,
                height = h)

label_dr.grid(row = 6, column = 0,columnspan=cs)
    
button_1 = Button(root,
                  text = "Card", 
                  font= font_1 ,
                  width = w,
                  height = h,
                  command = giveCard)

button_1.grid(row = 7, column = 0,columnspan=cs)

button_2 = Button(root,
                  text = "Stand", 
                  font= font_1 ,
                  width = w,
                  height = h,
                  command= stand)
button_2.grid(row = 8, column = 0,columnspan=cs)

button_3 = Button(root,
                  text = "Restart", 
                  font= font_1 ,
                  width = w,
                  height = h,
                  command = restart).grid(row = 9, column = 0,columnspan=cs)

result_label = Label(root,
               font= font_1 ,
                  width = w,
                  height = h,
                  bg = "brown",
                  justify = CENTER)

result_label.grid(row = 10, column = 0,columnspan=cs,pady = 5)

labelx = Label(root)
labelx.grid(row = 11,column = 0, rowspan= 10,columnspan = 10)


label_money = Label(labelx,
                    width = 40,
                    height = 2,
                    bg = "white",
                    font = "Ariel 15",
                    justify = CENTER)

label_money.grid(row = 0,column = 0,padx = 80)

label_money.configure(text = moneystr)
scale_widget = Scale(labelx, from_=0, to=1000, length = 300,
                             orient=HORIZONTAL)
scale_widget.set(500)
scale_widget.grid(row = 0,column = 1)



list1 = ["hearts","spades","diamonds","clubs"]
list2 = ["ace","king","queen","jack"]
list3 = []
list4 = []

for x in range(2,11):
    list2.append(str(x))
str1 = "_of_"

for x in list1:
    for y in list2:
        a = (str(y)+str1+x+".png")
        list3.append(a)



for x in range(4):
    for x in range(1,11):
        if x == 1:
            list4.append(11)
            list4.append(10)
            list4.append(10)
            list4.append(10)
        else:
            list4.append(x)
            
            
deck = dict(zip(list3,list4))

yourHand = []
yourResult = []
dealerHand = []
dealerResult = []
background = []
stop = False
win = False
lose = False


img2 = (Image.open("background.jpg"))
resized_image2 = img2.resize((125,181), Image.ANTIALIAS)
new_image2 = ImageTk.PhotoImage(resized_image2, master = root)
background.append(new_image2)

def checker():
    global win,lose
    if stop == False:
        if sum(yourResult) == 21 and len(yourResult) == 2:
            dealerCards()
            if sum(yourResult) == sum(dealerResult):
                result_label.configure(text = "Draw")
                
            else:
                result_label.configure(text = "BlackJack")
                win = True
                
        elif sum(yourResult) > 21:
            dealerCards()
            result_label.configure(text = " Too Many You Lost :(")
            lose = True
            button_1['state'] = DISABLED
            button_2['state'] = DISABLED
            

    elif stop == True:
        if sum(dealerResult) >21:
            result_label.configure(text = " Too Many You Win :)")
            win = True
        else:
            if sum(yourResult) > sum(dealerResult):
                result_label.configure(text = "You Win :)")
                win = True
            elif sum(yourResult) < sum(dealerResult):
                result_label.configure(text = "Lost :(")
                lose = True
            elif sum(yourResult) == sum(dealerResult):
                result_label.configure(text = "Draw :|")
            

def pickCard(num,w,h,liste,liste2):
    for x in range(num):

        randomCard = random.choice(list(deck.keys()))
        img = (Image.open(randomCard))
        resized_image = img.resize((w,h), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image, master = root)
        liste.append(new_image)
        liste2.append(deck[randomCard])
        

def result():
    if sum(yourResult) >21 and  11 in yourResult:
                
                for x in range(len(yourResult)):
                    if yourResult[x] == 11:
                        yourResult[x] = 1
                        break
    if sum(dealerResult) >21 and  11 in dealerResult:
                
                for x in range(len(dealerResult)):
                    if dealerResult[x] == 11:
                        dealerResult[x] = 1
                        break
    if stop == True:

        label_yr.configure(text = str(sum(yourResult)))
        label_dr.configure(text = str(sum(dealerResult)))
        
    else:
        label_yr.configure(text = str(sum(yourResult)))
        label_dr.configure(text = str(sum(dealerResult[:1])))
    checker()
    moneyCalculator()

def start():
    global labelCard_2,card_1,card_2

    pickCard(2,125,181,yourHand,yourResult)

    
    pickCard(2,125,181,dealerHand,dealerResult)

    for x in range(len(yourHand)):
        labelCard_2 = Label(root,
                  justify = CENTER,
                  image = yourHand[x])
        labelCard_2.grid(row = 2,column = x)
    
    for x in range(len(dealerHand)):
        if x == 0:
            card_1.configure(image = dealerHand[0])
        else:
            card_2.configure(image = background[0])
    result()

def moneyCalculator():
    global money
    a = scale_widget.get()
    
    if win == True:
        money += a
    elif lose == True:
        money -= a
    moneystr = str(money) + "$"
    label_money.configure(text = moneystr)
    print("your final money is " + moneystr)

    

start()
root.mainloop()