import subprocess, sys
import os
import tkinter as tk
from tkinter import messagebox



def RecycleEmpty():
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'ipconfig /all'])
       #a = subprocess.check_output([r'bat\IEbrow.bat'])
       a = subprocess.check_output(['powershell.exe','(New-Object -ComObject Shell.Application).NameSpace(0x0a).Items() | Select-Object Name,Size,Path'],shell=True) 
       
       a = a.decode("utf-8")
       #print(a)
       #a.replaceAll(" ", "")
       #b = a.replace(" ","")
       #print(a)
       #c = b.replace("NameDeviceID","")
       #d = c.replace("-","")
       #e = d.replace(" ","")
       #print(e)
       #test = len(e)
       #test1 = e.replace("CiscoAnyConnectSecureMobilityClientVirtualMiniportAdapterforWindowsx64ROOT\NET\0000","")
       #test1 = ""
       if(not a): 
           messagebox.showinfo("Result","passed") 
       else :
           messagebox.showerror("Result", "Failed")
           
       
       
