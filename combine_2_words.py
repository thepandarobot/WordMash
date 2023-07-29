import csv
import random
import tkinter as tk
from tkinter.ttk import *

def getMashedWords():
    filename = "/Volumes/T7/4_word_wordlist.csv"
    res=None

    with open(filename, 'r') as csvfile:
        wordscsv = list(csv.reader(csvfile))    

        lengthofcsv = len(wordscsv)
        position1 = random.randrange(0, lengthofcsv)
        position2 = random.randrange(0, lengthofcsv)

        my_pick = str(wordscsv[position1])
        my_pick2 = str(wordscsv[position2])
        my_pick = ''.join([i for i in my_pick if i.isalpha()])
        my_pick2 = ''.join([i for i in my_pick2 if i.isalpha()])
        res = my_pick + my_pick2
    return res

# Create Object
root = tk.Tk()

vartxt = None  
lb = None
 
# Set title
root.title("Mashed words")
 
# Set Geometry
root.geometry("800x200")
 

def launch():
    global vartxt
    res = getMashedWords()
    vartxt=tk.StringVar(value=res)
    global lb
    if lb != None:
        lb.destroy()
    lb=tk.Label(root, textvariable = vartxt,fg = "white",font = ("Times",40))
    lb.pack()
    root.update_idletasks()
 
 
# Add Buttons
tk.Button(root, text="Generate 2 word mashup", command=launch).pack(pady=10)

# Execute Tkinter
root.mainloop()
