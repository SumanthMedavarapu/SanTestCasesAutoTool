import subprocess
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import *

#root= tk.Tk()



def start_batch2(IEEntry):
    string = IEEntry.get()
    #print(string)
    try:
        val = int(string)
        #print(val)
        #print("Yes input string is an Integer.")
        #print("Input number value is: ", val)
        a = subprocess.check_output([r'bat\IE.bat'],shell=True)
        a = a.decode("utf-8")
        #print(a)
        regex = r"\.\d+"
        #print(regex)
        matches = re.findall(regex, a)
        #print(matches)
        converttostring = "".join(matches)
        matches1=string+converttostring
        
        
        if matches1 in a:
            messagebox.showinfo("Result","passed")
        else:
            messagebox.showerror("Result", "Failed")
        

    except ValueError:
        #print("That's not an int!")
        #print("No.. input string is not an Integer. It's a string")
        messagebox.showinfo("Warning!", "No.. input string is not an Integer. It's a string")
        IEEntry.delete(0, END)
