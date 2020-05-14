import tkinter as tk
from tkinter import filedialog, Text
import os
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DATINGAPP\SQLEXPRESS;'
                      'Database=datingapp;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM TestDB.dbo.Person')

for row in cursor:
    print(row)

root = tk.Tk()
root.geometry("800x800")
def getTextInput():
    result=textExample.get(1.0, tk.END+"-1c")
    print(result)



textExample=tk.Text(root, height= 1)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Naam", command=getTextInput)
btnRead.pack()
root.mainloop()
