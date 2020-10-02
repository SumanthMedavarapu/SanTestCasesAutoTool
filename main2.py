import subprocess
from tkinter import *
import tkinter as tk

#from checkbutton1 import *

from Qfepatch import *
from drivers2 import *
#from threading import *
#import main1
#from checkbutton import activateCheck
#global LAN,LANVar

#import checkbutton 
from tkinter import messagebox
from tkinter import *
#from PIL import ImageTk, Image
class ADVANCEGUI:
    def __init__(self,labelframe):
        #root= tk.Tk()
        #root.iconbitmap('mcd.ico')
        #root.title('McD')


        #labelframe = LabelFrame(master, text="Sanity Test Cases Automation Tool")
        #labelframe.grid(row = 0, column = 0)

        #logo = tk.PhotoImage(file="tenor.gif")

        #w1 = tk.Label(root, image=logo).pack(side="right")
        tk.Label(labelframe, text="Enter image version").grid(row=0,column=0)
        e1 = tk.Entry(labelframe)
        e1.grid(row=0, column=1)

        def show_entry_fields():
            print("Image version: %s" % (e1.get()))


        #tk.Button(labelframe, text='Test image version', command=show_entry_fields).grid(row=0, column=1, sticky=tk.W, pady=4)
        def printtext():
            #global ImgEnt
            string = ImgEnt.get() 
            if len(string) !=0:
                if string.count(".") == 2:
            #print(string)
                    decimal = string.split(".")
            #print(decimal)
    #a = subprocess.check_output([r'bat\IE.bat']).decode("utf-8") 
    #b = subprocess.check_output([r'bat\IE2.bat']).decode("utf-8")
    #c = subprocess.check_output([r'bat\IE1.bat']).decode("utf-8")
                    d = subprocess.check_output([r'bat\IE3.bat'],shell=True).decode("utf-8")
            #print(d)
                    d = d.replace(" ","")
                    f = d.split("REG_DWORD")
    #print(e)Dim wshshell wshshell.run cmd.exe  Display.bat
            #print(f[1][:3])
            #print(f[2][:3])
            #print(f[3][:3])
                    hexlist = [hex(int(x)) for x in decimal]
                    if (hexlist[0] in f[1][:3]) and (hexlist[1] in f[2][:3]) and (hexlist[2] in f[3][:3]):
                        messagebox.showinfo("Result","passed")
                    else:
                        messagebox.showerror("Result","failed")
                else:
                    e.delete(0, END)
                    messagebox.showinfo("Warning!", "Please enter correct image version")
            else:
            #TXE.delete(0, END)
                messagebox.showinfo("Warning!", "Box is empty! Write something")
            
       

        ImgVer = Label(labelframe, text="Enter image version")
        ImgVer.grid(row = 0, column = 0,padx = 10)




        ImgEnt = Entry(labelframe)
        ImgEnt.grid(row = 0, column = 1)
        #e.focus_set()

        b = Button(labelframe,text='check ImgVer',width = 12, height = 1,command=printtext)
        b.grid(row = 0, column = 2,padx = 10,pady = 1)
        #b.pack(side='top')

        DevVer = Label(labelframe, text="Enter Device version(for eg: 1.0")
        DevVer.grid(row = 1, column = 0,padx = 10)

        h = Entry(labelframe)
        h.grid(row = 1, column = 1)

        from Devicever import Devicever
        def printtext1():
            Devicever(h)

        c = Button(labelframe,text='check DeviceVer',width = 12, height = 1,command=printtext1)
        c.grid(row = 1, column = 2,padx = 10,pady = 1)






        from start_batch2 import start_batch2
        def printtext2():
            start_batch2(IEEntry)

           
        IELabel = Label(labelframe, text="Enter IE version(for eg: 11")
        IELabel.grid(row = 4, column = 0,padx = 10)
        IEEntry = Entry(labelframe)
        IEEntry.grid(row = 4, column = 1)

    
        IEButton = Button(labelframe,text='check IE',command=printtext2,width = 12, height = 1)
        IEButton.grid(row = 4, column = 2,padx = 10,pady = 1)

        from syserr import syserr
        def boo():
            syserr()

           
        button2 = tk.Button (labelframe, text='8:check Syserror',width = 20, height = 2,command=boo)
        button2.grid(row = 8, column = 0)

        from Useracc import Useracc
        def coo():
            Useracc()

           
        button3 = tk.Button (labelframe, text='12:check Useraccounts',width = 20, height = 2,command=coo)

        button3.grid(row = 12, column = 0)

        from Dupport import Dupport
        def doo():
            Dupport()

           
        button4 = tk.Button (labelframe, text='22:check Duplicateports',width = 20, height = 2,command=doo)

        button4.grid(row = 9, column = 2,padx = 10)

        from Netdhcp import Netdhcp
        def eoo():
            Netdhcp()

           
        button5 = tk.Button (labelframe, text='4:check dhcp',width = 20, height = 2,command=eoo)

        button5.grid(row = 5, column =0)

        from IEbrowsing import IEbrowsing
        def foo():
            IEbrowsing()

           
        button6 = tk.Button (labelframe, text='6:check Browsing history',width = 20, height = 2,command=foo)
        button6.grid(row = 6, column = 0)


        from DevExclam import DevExclam
        def goo():
            DevExclam()

           
        button7 = tk.Button (labelframe, text='7:check ! mark in devmgr',width = 20, height = 2,command=goo)
        button7.grid(row = 7, column = 0)

        from OpenReg import OpenReg
        def hoo():
            OpenReg()

           
        button8 = tk.Button (labelframe, text='9:check regedit',width = 20, height = 2,command=hoo)
        button8.grid(row = 9, column = 0)


        from RecycleEmpty import RecycleEmpty
        def ioo():
            RecycleEmpty()

           
        button9 = tk.Button (labelframe, text='10:check Recycle bin',width = 20, height = 2,command=ioo)
        button9.grid(row = 10, column = 0)


        from DisplayRes import DisplayRes
        def joo():
            DisplayRes()

           
        button10 = tk.Button (labelframe, text='16:check Disp Resol',width = 20, height = 2,command=joo)
        button10.grid(row = 6, column = 2,padx = 10,pady=2)


        from PowerPlan import PowerPlan
        def koo():
            PowerPlan()

           
        button11 = tk.Button (labelframe, text='26:check power plan',width = 20, height = 2,command=koo)
        button11.grid(row = 10, column = 2,padx = 10,pady=2)


        from Ethernet import Ethernet
        def loo():
            Ethernet()

           
        button12 = tk.Button (labelframe, text='27:check Ethernet',width = 20, height = 2, command=loo)
        button12.grid(row = 11, column = 2,padx = 10,pady=2)

        from Services import Services
        def moo():
            Services()

           
        button13 = tk.Button (labelframe, text='18:check Services',width = 20, height = 2, command=moo)
        #button13.grid(row = 5, column = 2)
        button13.grid(row = 8, column = 2,padx = 10,pady=2)

        from Qfepatch import Tabcal          
        button14 = tk.Button (labelframe, text='30:check Tabcal',width = 20, height = 2, command=Tabcal)
        button14.grid(row = 13, column = 2)
        from Qfepatch import RCbanne 
        button31 = tk.Button (labelframe, text='1:check RC banner',width = 20, height = 2, command=RCbanne)
        button31.grid(row = 14, column = 2)
        from Perm import Perm
        def poo():
            Perm()

           
        button15 = tk.Button (labelframe, text='14:check Permissions',width = 20, height = 2, command=poo)
        button15.grid(row = 5, column = 2,padx = 10)
        from Qfepatch import Qfepatch
        def qoo():
            Qfepatch()

           
        button16 = tk.Button (labelframe, text='17:check qfepatch',width = 20, height = 2, command=qoo)
        button16.grid(row = 7, column = 2,padx = 10)

        button17 = tk.Button (labelframe, text='13:check Kms',width = 20, height = 2, command=Kms)
        button17.grid(row = 13, column = 0)
        button27 = tk.Button (labelframe, text='29:check PortsRange',width = 20, height = 2, command=Ports)
        button27.grid(row = 12, column = 2,padx = 10)




        def new_window():
            GUI()
    
    
    

        button18 = tk.Button (labelframe, text='11:check Drivers',width = 20, height = 2, command=new_window)
        button18.grid(row = 11, column = 0)
        #def on_closing():
        #    if messagebox.askokcancel("Exit","Are You Sure?"):
        #        root.destroy()







        #root.protocol("WM_DELETE_WINDOW",on_closing)
