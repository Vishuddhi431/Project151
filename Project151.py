#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 08:13:18 2023

@author: vishuddhimakeshwaran
"""
from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Project 151")

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (2, 4.5, 1, 0.5, 6, 8, 4, 5.5, 9, 5.5, 3, 2)

labelMonths = Label(root)
labelMonths.place(relx = 0.5, rely = 0.3, anchor = CENTER)
labelMonths["text"] = "Months: " + str(months)

labelProfits = Label(root)
labelProfits .place(relx = 0.5, rely = 0.4, anchor = CENTER)
labelProfits["text"] = "Profits: " + str(profits)

labelAns1 = Label(root)
labelAns1.place(relx = 0.5, rely = 0.6, anchor = CENTER)

labelAns2 = Label(root)
labelAns2.place(relx = 0.5, rely = 0.8, anchor = CENTER)

def minProfit(): 
    minProfit = min(profits)
    print(minProfit)
    indexMin = profits.index(minProfit)
    print(indexMin)
    print("The min profit of " + str(minProfit) + " million occured in the month of " + str(months[indexMin]))
    labelAns2["text"] = "The min profit of " + str(minProfit) + " million occured in the month of " + str(months[indexMin])
    
def maxProfit(): 
    maxProfit = max(profits)
    print(maxProfit)
    indexMax = profits.index(maxProfit)
    print(indexMax)
    print("The max profit of " + str(maxProfit) + " million occured in the month of " + str(months[indexMax]))
    labelAns1["text"] = "The max profit of " + str(maxProfit) + " million occured in the month of " + str(months[indexMax])


button1 = Button(root, text = "Show max profitable month", command = maxProfit)
button1.place(relx = 0.5, rely = 0.5, anchor = CENTER)

button2 = Button(root, text = "Show min profitable month", command = minProfit)
button2.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()

