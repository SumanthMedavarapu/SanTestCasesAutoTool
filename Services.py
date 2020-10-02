import subprocess,sys
import tkinter as tk
from tkinter import messagebox

#root= tk.Tk()
 


def Services():



        a= subprocess.check_output(['powershell.exe', 'get-service UI0Detect | select Displayname,Status,ServiceName,Can*;Get-Service UI0Detect | select -property name,starttype;get-service Spooler | select Displayname,Status,ServiceName,Can*;Get-Service Spooler | select -property name,starttype;Get-Service W32Time | select -property name,starttype;Get-Service wuauserv | select -property name,starttype;Get-Service MpsSvc | select -property name,starttype;get-service MpsSvc | select Displayname,Status,ServiceName,Can*;Get-NetFirewallProfile -All'],shell=True).decode("utf-8")
        b = a.replace(" ","")
        #print(b)
        #print(b.count('Status:Running'))#3 finished
        #print(b)
        c = ["""DisplayName:InteractiveServicesDetection
Status:Running""","""Name:W32Time
StartType:Automatic""","""Name:UI0Detect
StartType:Manual(Trigger Start)""","""DisplayName:PrintSpooler

        Status:Running""","""Name:Spooler
StartType:Automatic""","""Name:wuauserv
StartType:Automatic""","""Name:MpsSvc

        StartType:Automatic""","""DisplayName:WindowsDefenderFirewall

        Status:Running""","Enabled:False"]
        

        a_match = [True for match in c if match in b]

        if True in a_match:
            messagebox.showinfo("Result","passed")
        else:
            messagebox.showerror("Result", "Failed")
        
       
       
        

       
       
       #b = subprocess.call([r'powershell\Services.ps1'])
       #a= subprocess.check_output(['regedit.exe', 'reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer" /v version'])
       #a= subprocess.check_output(['powershell.exe', 'get-service UI0Detect | select Displayname,Status,ServiceName,Can*']).decode("utf-8")
       #a= a + subprocess.check_output(['powershell.exe', 'Get-Service UI0Detect | select -property name,starttype']).decode("utf-8")
       #a= a + subprocess.check_output(['powershell.exe', 'get-service Spooler | select Displayname,Status,ServiceName,Can*']).decode("utf-8")
       #a= a + subprocess.check_output(['powershell.exe', 'Get-Service Spooler | select -property name,starttype']).decode("utf-8")
       #a= a + subprocess.check_output(['powershell.exe', 'Get-Service W32Time | select -property name,starttype']).decode("utf-8")
       #a= a + subprocess.check_output(['powershell.exe', 'Get-Service wuauserv | select -property name,starttype']).decode("utf-8")
       #a= a + subprocess.check_output(['powershell.exe', 'Get-Service MpsSvc | select -property name,starttype']).decode("utf-8")
       #a= a + subprocess.check_output(['powershell.exe', 'get-service MpsSvc | select Displayname,Status,ServiceName,Can*']).decode("utf-8")
       #a= a + subprocess.check_output(['powershell.exe', 'Get-NetFirewallProfile -All']).decode("utf-8")
       #b = a.replace(" ","")
       
       
       #print(b.count('Status:Stopped'))
       #print(a)
       #if ('DisplayName:InteractiveServicesDetection', 'Status:Stopped') in b:
       #    messagebox.showinfo("Result","passed")
       #else:
        #   messagebox.showerror("Result", "Failed")
           

       










       #print(a)
       #if a.find('9.11.10586.1'):
        #   print("success")
       #else:
        #   print("failed")
       #root = tk.Tk()
       #root.withdraw()


       #if "9.11.16299.0" in a:
        #   messagebox.showinfo("Result","passed")
       #else:
        #   messagebox.showerror("Result", "Failed")
