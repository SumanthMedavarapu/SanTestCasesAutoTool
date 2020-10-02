import subprocess, sys
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
#root= tk.Tk()


def Devicever(h):
    
    #global h
    
    
    string = h.get()
    if len(string) !=0:
        if string.count(".") == 1:
            #print(string)
            decimal = string.split(".")
            #print(decimal)
    #a = subprocess.check_output([r'bat\IE.bat']).decode("utf-8") 
    #b = subprocess.check_output([r'bat\IE2.bat']).decode("utf-8")
    #c = subprocess.check_output([r'bat\IE1.bat']).decode("utf-8")
            d = subprocess.check_output([r'bat\Dp.bat'],shell=True).decode("utf-8")
            #print(d)
            d = d.replace(" ","")
            f = d.split("REG_DWORD")
            hexlist = [hex(int(x)) for x in decimal]
            if (hexlist[0] in f[1][:3]) and (hexlist[1] in f[2][:3]):
                #APP_XPOS=10
                #APP_YPOS=2
                messagebox.showinfo("Result","passed")
                #messagebox.showinfo("Result","PASS:{}\nFAIL:{}".format(APP_XPOS, APP_YPOS))
            else:
                messagebox.showerror("Result","failed")
        else:
            h.delete(0, END)
            messagebox.showinfo("Warning!", "Please enter correct device version")
    else:
            #TXE.delete(0, END)
        messagebox.showinfo("Warning!", "Box is empty! Write something")

    #print(f)Dim wshshell wshshell.run cmd.exe  Display.bat
            #print(f[1][:3])
            #print(f[2][:3])
    
    """str="".join(d[1:193])
    print(str)
    str1="".join(d[194:386])
    print(str1)
    str2="".join(d[387:])"""

            

    #print(hexlist[0])
    #print(hexlist[1])
    #print(hexlist[2])
    #if (hexlist[0] in str) and (hexlist[1] in str1)):
     #   messagebox.showinfo("Result","passed")
   # else:
    #    messagebox.showerror("Result","failed")
    
