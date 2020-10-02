import subprocess, sys
import os
import tkinter as tk
from tkinter import messagebox



def Netdhcp():
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'ipconfig /all'])
       a = subprocess.check_output([r'bat\Dhcp.bat'],shell=True)
       #a = subprocess.check_output(['powershell.exe','Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=TRUE -ComputerName']) 
       #print(a)
       a = a.decode("utf-8")
       #print(a)
       s = a.replace(". ", "")
       p = s.replace(": ", "")
       
       #print(p)
       if "DHCP EnabledYes" in p:
           messagebox.showinfo("Result","passed")
       else:
           messagebox.showerror("Result", "Failed")

      # m = a.count("Administrator")
      # print(m)
      # if "DHCP EnabledYes" is 1:
       #    messagebox.showinfo("Result","passed")
       #else:
        #   messagebox.showerror("Result", "Failed")    
