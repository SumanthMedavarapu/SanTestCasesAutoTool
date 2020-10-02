import subprocess, sys
import os
import tkinter as tk
from tkinter import messagebox



def OpenReg():
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'regedit'])
       subprocess.call([r'bat\Reg.bat'],shell=True)
       #a = subprocess.check_output([r'bat\IEbrow.bat'])
       #a = subprocess.check_output(['powershell.exe','Get-WmiObject Win32_PNPEntity | Where-Object{$_.ConfigManagerErrorCode -ne 0} | Select Name, DeviceID']) 
       
       #a = a.decode("utf-8")
      # print(a)
       #a.replaceAll(" ", "")
      # b = a.replace(" ","")
       #c = b.replace("NameDeviceID","")
      # d = c.replace("-","")
       #e = d.replace(" ","")
       #print(e)
       #test = len(e)
       #test1 = e.replace("CiscoAnyConnectSecureMobilityClientVirtualMiniportAdapterforWindowsx64ROOT\NET\0000","")
       #test1 = ""
       #if(not d.strip()): 
         #  messagebox.showinfo("Result","passed") 
       #else :
         #  messagebox.showerror("Result", "Failed")
           
       
       
