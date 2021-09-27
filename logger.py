# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 01:17:15 2020

@author: Samuel James
"""

from tkinter import *
from datetime import date
import csv 
today = date.today()
d1 = today.strftime("%d/%m/%Y")

root=Tk()
def retrieve_input():
    inputValue1=textBox1.get("1.0","end-1c")
    inputValue2=textBox2.get("1.0","end-1c")
    inputValue3=textBox3.get("1.0","end-1c")
    inputValue4=textBox4.get("1.0","end-1c")
    inputValue5=textBox5.get("1.0","end-1c")
    
    with open('DailyLog.csv', 'a', newline='') as df:
        writer = csv.writer(df)
        df.write(inputValue1 + ',')
        df.write(inputValue2 + ',')
        df.write(inputValue3 + ',')
        df.write(inputValue4 + ',')
        df.write(inputValue5 + ',')
        df.write(d1 + ',')
        writer.writerow('')
    df.close()
    root.destroy()
    
labelText=StringVar()
labelText.set("Happiness(1-10): ")
labelDir=Label(root, textvariable=labelText)
labelDir.pack()

textBox1=Text(root, height=1, width=10)
textBox1.pack()

labelText2=StringVar()
labelText2.set("pain(1-10): ")
labelDir2=Label(root, textvariable=labelText2)
labelDir2.pack()

textBox2=Text(root, height=1, width=10)
textBox2.pack()

labelText3=StringVar()
labelText3.set("Did you eat Bkfst? (Y/N): ")
labelDir3=Label(root, textvariable=labelText3)
labelDir3.pack()

textBox3=Text(root, height=1, width=10)
textBox3.pack()

labelText4=StringVar()
labelText4.set("Cardio? (Y/N):  ")
labelDir4=Label(root, textvariable=labelText4)
labelDir4.pack()

textBox4=Text(root, height=1, width=10)
textBox4.pack()

labelText5=StringVar()
labelText5.set("Choose a number: ")
labelDir5=Label(root, textvariable=labelText5)
labelDir5.pack()

textBox5=Text(root, height=1, width=10)
textBox5.pack()


buttonCommit=Button(root, height=1, width=10, text="Commit", command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button

buttonCommit.pack()

mainloop()
