import subprocess, sys
import os
import tkinter as tk
from tkinter import messagebox



def IEbrowsing():
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'ipconfig /all'])
       a = subprocess.check_output([r'bat\IEbrow.bat'],shell=True)
       #a = subprocess.check_output([r'powershell\Untitled3.ps1'])
       #a = subprocess.check_output(['powershell.exe','Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=TRUE -ComputerName']) 
       
       b = a.decode("utf-8")
       c = b.replace(" ","")
       #print(c)
       
       
       
       
       if "CouldnotdisplaytheDNSResolverCache." in c:
           messagebox.showinfo("Result","passed")
       else:
           messagebox.showerror("Result", "Failed")
