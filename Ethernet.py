import subprocess, sys
import os
import tkinter as tk
from tkinter import messagebox







def Ethernet():
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       a= subprocess.check_output(['powershell.exe', 'Get-NetIPConfiguration | select InterfaceAlias'],shell=True)      
       a = a.decode("utf-8")
       Replac = a.replace("InterfaceAlias","")
       Replace1 = Replac.replace("-","")
       Replace2 = Replace1.replace(" ","")
       #print(Replace2)
       list = Replace2.split()
       #print(list)
       checkstrings=['Ethernet','Ethernet2']
       #list1=['Ethernet','rh','jsdg']
       count = 0
       if len(list) > 2:
           #print("Fail")
           messagebox.showerror("Result","Failed")
       elif len(list) ==2 :
           for lis in checkstrings:
               if lis in Replace2:
                   count +=1
               else:
                   messagebox.showerror("Result", "Failed")

           
       else:
           if "Ethernet" in list:
               #print("pass")
               messagebox.showinfo("Result","passed")
           else:
               messagebox.showerror("Result", "Failed")
       if count ==2:
           #print("pass")
           messagebox.showinfo("Result","Passed")
                  
       #print(a)
       




              
