import subprocess, sys
import os
import tkinter as tk
from tkinter import messagebox



def Perm():
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'ipconfig /all'])
       #a = subprocess.check_output([r'bat\PM.bat'])
       #a = subprocess.check_output([r'bat\IE.bat'])
       a = subprocess.check_output(['powershell.exe','Get-Acl C: | select AccessToString | fl;Get-Acl D: | select AccessToString | fl;Get-Acl E: | select AccessToString | fl'],shell=True) 
       
       a = a.decode("utf-8")
       #print(a)
       b = a.replace(" ", "")
       #print(b)
       split = b.split("AccessToString:")
       #print(split[1])
       #print(split[2])
       #print(split[3])
       list = ["NTAUTHORITY\AuthenticatedUsersAllowModify","NTAUTHORITY\SYSTEMAllowFullControl","BUILTIN\AdministratorsAllowFullControl","BUILTIN\\UsersAllowModify"]
       mylistlength = len(split)
       #print(mylistlength)
       counter = 0
       list1 = ["BUILTIN\\UsersAllowFullControl","NTAUTHORITY\AuthenticatedUsersAllowFullControl"]
       counter1 = 0
       for lis in list1:
              for i in range(1,mylistlength):
                  if lis in split[i]:
                      counter1+=1
                     

       """for li in list:
              for i in range(1,mylistlength-1):
                     if li in split[i]:
                            counter+=1
                            #messagebox.showinfo("Result","passed")"NTAUTHORITY\AuthenticatedUsersAllowFullControl",
                     else:
                            messagebox.showerror("Result","Failed")"""
       
       #messagebox.showerror("Result","Failed")
       for i in range(1,mylistlength):
              for li in list:
                     if not(counter == 8 or counter ==11):
                         if li in split[i]:
                             counter+=1
                         else:
                                messagebox.showerror("Result","Failed")
                                
                                
                     else:
                            counter+=1
                            
       if counter1 == 0 and counter == 12:     
              messagebox.showinfo("Result","passed")
       else:
              messagebox.showerror("Result","Failed") 
              
              
       
                     
              
        
               
               
              
                            
              
              
       #print(c)
       #if "7681024" in b:
       #    messagebox.showinfo("Result","passed")
       #else:
        #   messagebox.showerror("Result","Failed")
           
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
