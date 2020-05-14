import tkinter as tk
from tkinter import filedialog, Text
import os
import pyodbc
root = tk.Tk()
root.title("DatingAAP")
root.geometry("600x400")
#userdb = 'datingapp.dbo.persgegevens(voornaam, lidnummer)'
#questdb = 'datingapp.dbo.quizvragen()'
#chosendb = 'nog niks'
conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DATINGAPP;'
                          'Database=datingapp;'
                          'UID=computerland;''PWD=P@ssw0rd')

cursor = conn.cursor()
def getTextInput():
    result=textExample.get(1.0, tk.END+"-1c")

    cursor.execute(result)
    conn.commit()



textExample=tk.Text(root, height= 1)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Naam", command=getTextInput)
btnRead.pack()

AntwoordA=tk.Button(root, height=2, width=20, text="A").place(x=10, y=350)


AntwoordB=tk.Button(root, height=2, width=20, text="B").place(x=225, y=350)


AntwoordC=tk.Button(root, height=2, width=20, text="C").place(x=440, y=350)


root.mainloop()


def insertdb(chosendb):
    cursor.execute('INSERT INTO'+ chosendb + 'VALUES' () )

    return;




