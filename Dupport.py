import subprocess, sys
import os
import tkinter as tk
from tkinter import messagebox







def Dupport():
       #log = open("log.txt", "a")
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a= subprocess.check_output(['powershell.exe','-WindowStyle ','hidden','-command','Get-WmiObject Win32_SerialPort | Select-Object deviceid '])
       #a= subprocess.check_output(['powershell.exe','-nologo','Get-WmiObject Win32_SerialPort | Select-Object deviceid '])
       a= subprocess.check_output(['powershell.exe','-WindowStyle ','hidden','Get-WmiObject Win32_SerialPort | Select-Object deviceid '],shell=True)
       
       a = a.decode("utf-8")
       #print(a)
       words = a.split()
       #words = ['deviceid', '--------', 'COM3', 'COM1','COM1','COM3']
       counts = {}
       for word in words:
           if word not in counts:
               counts[word] = 0
           counts[word] += 1
       #print(counts)
       #print(counts.values())
       count = 0
       for key, value in counts.items():
           if value > 1:
               count +=1
              
              
                     
       if count == 0:
              messagebox.showinfo("Result","passed")
              #log.write(str('\n[OKdupport]'))
       else:
              messagebox.showerror("Result", "Failed")
              #log.write(str('\n[faildupport]'))
       #log.close()
              
                    
       #for value in counts.values():
       #if "Error" in a:
        #      messagebox.showerror("Result", "Failed")
       #else:
       #        messagebox.showinfo("Result","passed")
