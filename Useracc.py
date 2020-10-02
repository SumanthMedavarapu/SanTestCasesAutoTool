import subprocess, sys
import os
import tkinter as tk
from tkinter import messagebox


def Useracc():
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       a = subprocess.check_output(['powershell.exe', 'net user'],shell=True)      
       a = a.decode("utf-8")
       #print(a)
       #s = a.replace(" ", "")
       #print(s)

       m = a.count("Administrator")
       print(m)
       if m is 1:
           messagebox.showinfo("Result","passed")
       else:
           messagebox.showerror("Result", "Failed")    




       
       #if b is 1:
       #    messagebox.showinfo("Result","passed")
       #else:
       #    messagebox.showerror("Result", "Failed")
           
       #if "Error" in a:
        #      messagebox.showerror("Result", "Failed")
       #else:
        #       messagebox.showinfo("Result","passed")
