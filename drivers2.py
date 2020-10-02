from tkinter import *
import subprocess, sys
import os
from tkinter.ttk import Combobox
#from threading import *

from tkinter import messagebox
import tkinter as tk
    

"""class karl( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)"""


def Drivers1():
    #print(cb.get())
    str = cb.get()            
    """for lis in mylist2: 
        if str in lis:
            regex = r"\d+\.\d+\.\d+\.\d+"
            
            #print(regex1)
            matches = re.findall(regex, lis)
            
            if len(matches) == 0:
                regex1 = r"\d+\.\d+\.\d+"
                matches1 = re.findall(regex1, lis)
                messagebox.showinfo("Result",matches1)
                
            else:
                messagebox.showinfo("Result",matches)"""
    for getonestring in conlist2:
        if str in getonestring:
            print(getonestring)
            print(str)
            #matches1=remove(str,getonestring)
            matches1=getonestring.replace(str,'')
            messagebox.showinfo("Result",matches1)
                
                
                
            
             
            

            

                
def Drivers():
    global cb
    #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
    #a = subprocess.check_output(['cmd.exe', 'ipconfig /all'])
    """d = subprocess.check_output([r'bat\CP.bat']).decode("utf-8")
    a = subprocess.check_output(['powershell.exe','-WindowStyle','hidden','Get-Wmiobject Win32_PnPSignedDriver|select DeviceName,DriverVersion']) 
       
    a = a.decode("utf-8")
    str1= d.replace(" ", "")
    #print(str1)
    str2 = a.replace(" ", "")
    #print(str2)
    #str3="".join(str1)
    #str4="".join(str2)"""
    string = LAN.get()
    newstring1 ="" 
    for a in string: 
        if a.isnumeric() == False: 
            newstring1+= a
    
    new = newstring1[0:-3]
    print(new)
    
   
    
    if len(string) !=0:
        if string.count(".") == 3:
            d = subprocess.check_output([r'bat\CP.bat'],shell=True).decode("utf-8")
            d = subprocess.check_output([r'bat\CP1.bat'],shell=True).decode("utf-8")
            a = subprocess.check_output(['powershell.exe','Get-Wmiobject Win32_PnPSignedDriver|select DeviceName'],shell=True)
            a = subprocess.check_output(['powershell.exe','Get-Wmiobject Win32_PnPSignedDriver|select DriverVersion'],shell=True)
       
            a = a.decode("utf-8")
            str1= d.replace(" ", "")
            str2 = a.replace(" ", "")
            b = ""+str1+str2
            print(b)
            if new in b:
                if string in b:
                    LAN.delete(0, END)
                    messagebox.showinfo("Result","passed")
                else:
                    LAN.delete(0, END)
                    messagebox.showerror("Result", "Failed")
            else:
                messagebox.showinfo("Warning!", "driver is not installed")
            
                
            
                

        else:
            LAN.delete(0, END)
            messagebox.showinfo("Warning!", "Please enter correct driver version")
    else:
            #TXE.delete(0, END)
        messagebox.showinfo("Warning!", "Box is empty! Write something")

        
class GUI():
    def __init__(self):
        global LAN,cb,conlist2
        win = Tk()
        #win.update()
        
        win.attributes("-topmost", True)

        win.iconbitmap('mcd.ico')
        win.title('McD')
        win.geometry("520x150")
        #d = subprocess.check_output([r'bat\CP.bat']).decode("utf-8")
        conname = subprocess.check_output([r'bat\CP.bat'],shell=True).decode("utf-8")
        conver = subprocess.check_output([r'bat\CP1.bat'],shell=True).decode("utf-8")
        devname= subprocess.check_output(['powershell.exe','Get-Wmiobject Win32_PnPSignedDriver|select DeviceName'],shell=True).decode('utf-8')
        devver = subprocess.check_output(['powershell.exe','Get-Wmiobject Win32_PnPSignedDriver|select DeviceName,DriverVersion'],shell=True).decode('utf-8')
        rep = conname.replace(" ","")
        rep2 = devname.replace(" ","")
        #d = subprocess.check_output([r'bat\CP1.bat'],shell=True).decode("utf-8")
        #a = subprocess.check_output(['powershell.exe','-WindowStyle','hidden','Get-Wmiobject Win32_PnPSignedDriver|select DeviceName,DriverVersion'],shell=True).decode('utf-8')
        llist=rep.split()
        del llist[0:2]
        #print(list)
        list1=rep2.split()
        del list1[0:2]
        #print(list1)
        lis2=list1+llist
        list2 = list(dict.fromkeys(lis2))
        #print(list2)
        
        
        rep3 = conver.replace(" ","")
        rep4 = devver.replace(" ","")
        conlist=rep3.split()
        del conlist[0:2]
        #print(list)
        conlist1=rep4.split()
        del conlist1[0:2]
        #print(list1)
        conlis2=conlist1+conlist
        #print(conlis2)
        conlist2 = list(dict.fromkeys(conlis2))
        #print(conlist2)
        
       
        

        
        """str =d.replace(" ", "")
        h = str.split()
        del h[0:2]
        #print(h)
        mylist = list(dict.fromkeys(h))
        print(mylist)
        list2=[]


        newstring = ""  
        for lis in mylist: 
            for str in lis:
        
                if (str.isnumeric() == False) and  ("." not in str):
                    newstring += str
    #newstring.replace(".","")
    #newstring.translate({ord('.'): None})
            list2.append(newstring)
            newstring = ""

        #print(f)
        #a = subprocess.check_output(['powershell.exe','-WindowStyle','hidden','Get-Wmiobject Win32_PnPSignedDriver|select DeviceName,DriverVersion']).decode('utf-8')
        #print(a)
        str1 =a.replace(" ", "")
        
        h1 = str1.split()
        #print(h)
        
        del h1[0:2]
        mylist1 = list(dict.fromkeys(h1))
        print(mylist1)
        list1=[]


        newstring1 = ""  
        for lis in mylist1: 
            for str1 in lis:
        
                if (str1.isnumeric() == False) and  ("." not in str1):
                    newstring1 += str1
    #newstring.replace(".","")
    #newstring.translate({ord('.'): None})
            list1.append(newstring1)
            newstring1 = ""
        list2 = list2 + list1"""
        list3 =  sorted(list2)

        data=["one", "two", "three", "four"]
        #frame_name=Toplevel(win)
        cb=Combobox(win, values=list3,width=40)
        cb.grid(row=1,column=2)
        #app = Frame(master,height=50, width=50);
        #app.grid();
        #right = Frame(master, height=100, width=100)
        #right.grid(row=,column=5)
        #master.title("Driver")
        
        Label(win, text="Please select driver name").grid(row=1, column=1)
        #LAN = Entry(frame_name)
        #LAN.grid(row=0, column=2)
        button7 = Button (win, text=' Test drivers',width = 15, height = 2,command=Drivers1)
        button7.grid(row = 1, column = 3)
        #frame_name.grid(row=0,column=0)
        





