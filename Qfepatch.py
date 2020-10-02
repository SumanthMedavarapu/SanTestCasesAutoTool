import subprocess, sys
import os
import tkinter as tk
from tkinter import messagebox



def Qfepatch():
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'wmic qfe list']).decode("utf-8")
       #a = subprocess.check_output([r'bat\qfe.bat']).decode("utf-8")
       subprocess.call([r'bat\qfe.bat'])
       #a = subprocess.check_output(['powershell.exe','Get-Acl C: | select AccessToString | fl;Get-Acl D: | select AccessToString | fl;Get-Acl E: | select AccessToString | fl']) 
       #print(a)
       """a = a.decode("utf-8")
       print(a)
       b = a.replace(" ", "")
       #print(b)
       split = b.split("AccessToString:")
       print(split[1])
       print(split[2])
       print(split[3])"""

def RCbanne():
       RC = subprocess.check_output([r'bat\RC.bat'],shell=True).decode("utf-8")
       #print(RC)
       if "Release Candidate" in RC:
           messagebox.showerror("Result", "Failed")
       else:
           messagebox.showinfo("Result","passed")
       


def Kms():
       a = subprocess.check_output([r'bat\Kms.bat'],shell=True).decode("utf-8")
       #a = subprocess.check_output(['powershell.exe','Get-Acl C: | select AccessToString | fl;Get-Acl D: | select AccessToString | fl;Get-Acl E: | select AccessToString | fl']) 
       #print(a)

def Tabcal():
       #a = subprocess.check_output([r'bat\tab.bat']).decode("utf-8")
       subprocess.call([r'bat\tab.bat'],shell=True)
       #a = subprocess.check_output(['powershell.exe','Get-Acl C: | select AccessToString | fl;Get-Acl D: | select AccessToString | fl;Get-Acl E: | select AccessToString | fl']) 
       

def Ports():
       port = subprocess.check_output([r'bat\Ports.bat'],shell=True).decode("utf-8")
       #a = subprocess.check_output(['powershell.exe','Get-Acl C: | select AccessToString | fl;Get-Acl D: | select AccessToString | fl;Get-Acl E: | select AccessToString | fl']) 
       #print(a)
       #port = "hai 5001-5150"
       if "5001-5150" in port:
           messagebox.showinfo("Result","passed")
       else:
           messagebox.showerror("Result", "Failed")
           
       
