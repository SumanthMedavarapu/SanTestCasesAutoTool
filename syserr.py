import subprocess, sys
import os
import tkinter as tk
from tkinter import messagebox

#root= tk.Tk()




       #a = subprocess.check_output([r'powershell\syserror.ps1'])
       #a = a.decode("utf-8")
       #print(a)
       #process=subprocess.Popen(["powershell","Get-EventLog -LogName System -EntryType Error"],stdout=subprocess.PIPE);
       #result=process.communicate()[0]
       #print(result)
       #p = subprocess.Popen(["powershell.exe", 
        #      "powershell\syserr.ps1"], 
        #      stdout=sys.stdout)
      # p.communicate()
       #print(p)
       #a = subprocess.check_output([r'powershell\syserror.ps1'])
       #a = a.decode("utf-8")
       #print(a)
       #print(a)
       #if a.find('9.11.10586.1'):
        #   print("success")
       #else:
        #   print("failed")
       #root = tk.Tk()
       #root.withdraw()


       #if "9.11.10586.0" in a:
           #messagebox.showinfo("Result","passed")
       #else:
           #messagebox.showerror("Result", "Failed")

 


       
 
def syserr1():
       powerShellPath = r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe'
       powerShellCmd = "powershell\syserror.ps1"
 
       p = subprocess.Popen([powerShellPath, '-ExecutionPolicy', 'Unrestricted', powerShellCmd, 'HELLO', 'WORLD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       output, error = p.communicate()
       rc = p.returncode
       print ("Return code given to Python script is: " + str(rc))
       print ("\n\nstdout:\n\n" + str(output))
       print ("\n\nstderr: " + str(error))


def syserr():
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       a= subprocess.check_output(['powershell.exe', 'Get-EventLog -LogName System -EntryType Error'],shell=True)      
       a = a.decode("utf-8")
       #print(a)
       if "Error" in a:
           messagebox.showerror("Result", "Failed")
       else:
           messagebox.showinfo("Result","passed")
           
       
       
 
