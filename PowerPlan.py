import subprocess, sys
import os
import tkinter as tk
from tkinter import messagebox
 
 
 
  
 








def PowerPlan():
       #log = open("log.txt", "a")
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a= subprocess.check_output(['powershell.exe','-WindowStyle ','hidden','-command', 'powercfg -list '])
       #a= subprocess.check_output(['powershell.exe','-nologo', 'powercfg -list '])
       a= subprocess.check_output(['powershell.exe','powercfg -list '],shell=True)
       
       a = a.decode("utf-8")
       #print(a)
       b = a.replace(" ","")
       
       #print(b)
       if "(McDonald'sPowerPlan)*" in b:
              messagebox.showinfo("Result","passed")
              #log.write(str('\n[OKpowerplan]'))
              
       else:
              messagebox.showerror("Result", "Failed")
              #log.write(str('\n[FAILpowerplan]'))
       #log.close()
              
       
              
              
      
