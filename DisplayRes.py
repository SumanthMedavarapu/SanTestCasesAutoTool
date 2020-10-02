import subprocess, sys
import os
import tkinter as tk
from tkinter import messagebox



def DisplayRes():
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'ipconfig /all'])
       #a = subprocess.check_output([r'bat\Display.bat'])
       a = subprocess.check_output(['powershell.exe','Get-WmiObject -class "Win32_DisplayConfiguration" | select PelsHeight,PelsWidth'],shell=True) 
       #subprocess.call(['powershell.exe','Get-WmiObject -class "Win32_DisplayConfiguration" | select PelsHeight,PelsWidth']) 

       a = a.decode("utf-8")
       print(a)
       b = a.replace(" ", "")
       print(b)
       if "7681024" in b:
           messagebox.showinfo("Result","passed")
       else:
           messagebox.showerror("Result","Failed")
           
       #b = a.replace(" ","")
       #c = b.replace("NameDeviceID","")
       #d = c.replace("-","")
       #e = d.replace(" ","")
       #print(e)
       #test = len(e)
       #test1 = e.replace("CiscoAnyConnectSecureMobilityClientVirtualMiniportAdapterforWindowsx64ROOT\NET\0000","")
       #test1 = ""
       #if(not d.strip()): 
       #    messagebox.showinfo("Result","passed") 
      # else :
        #   messagebox.showerror("Result", "Failed")
           
       
       
