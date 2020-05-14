import tkinter as tk
from tkinter import filedialog, Text
import os
import pyodbc
root = tk.Tk()
root.geometry("800x800")

def getTextInput():
    result=textExample.get(1.0, tk.END+"-1c")
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DATINGAPP;'
                          'Database=datingapp;'
                          'UID=computerland;''PWD=P@ssw0rd')

    cursor = conn.cursor()
    cursor.execute(result)
    for row in cursor:
        print(row)



textExample=tk.Text(root, height= 1)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Naam", command=getTextInput)
btnRead.pack()
root.mainloop()





