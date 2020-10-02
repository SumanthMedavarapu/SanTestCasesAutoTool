from progressbar1 import *
from tkinter import ttk
from tkinter.ttk import Combobox
import os
import time
import re
import subprocess
#import threading
from tkinter import *
from BasicUIfunctions import *
from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Progressbar
from tkinter import messagebox

from main2 import *

from tkinter import filedialog
import pandas as pd
def drivers1():
    df['Driver Name'] = df['Driver Name'].str.replace(" ","")
        
        
    get_cp_data = subprocess.check_output([r'bat\CP1.bat']).decode("utf-8")
    get_devmgr_data = subprocess.check_output(['powershell.exe','-WindowStyle','hidden','Get-Wmiobject Win32_PnPSignedDriver|select DeviceName,DriverVersion']).decode('utf-8')
    #e = get_cp_data + get_devmgr_data
    cp_rm_spaces = get_cp_data.replace(" ","")
    devmgr_rm_spaces = get_devmgr_data.replace(" ","")
    cp_list_data=cp_rm_spaces.split()
    del cp_list_data[0:2]
        #print(list)
    devmgr_list_data=devmgr_rm_spaces.split()
    del devmgr_list_data[0:2]
        #print(list1)
    complete_list_data=devmgr_list_data+cp_list_data
    #print(complete_list_data)
    convert_to_dict = list(dict.fromkeys(complete_list_data))
    #print(convert_to_dict)
    print(len(convert_to_dict))

    #drivernamelist=[]
    #driverversionlist=[]
    
    sum = df['Driver Name'] + df['Version']
    drivname1 = df['Driver Name']
    drivname = str(drivname1)
    print(type(drivname))
    print(type(convert_to_dict))
    #print(drivname)
    versionnumber = df['Version']
        #sum is input from excel file
    #print(sum)
    #print(sum[0])
        #sum[6]="MicrosoftKernelDebugNetworkAdapter10.0.14393.0"
    mylistlength = len(sum)
    i = 0
    while i < mylistlength:
        matching = [s for s in convert_to_dict if drivname[i] in s]
        i+=1
    print(len(matching))    
    result=[]
    
    while i < mylistlength:
        for getonelistvalue in convert_to_dict:
            if drivname[i] in getonelistvalue:
                if (drivname[i] in getonelistvalue) and (versionnumber[i] in getonelistvalue) :
                    #result[i]="Pass"
                    result.append("pass")
                
                #else:
                   # result.append("Fail")
            #else:
                #result[i]="Driver not installed"
               # result.append("driver not installed")
        i += 1 

  
        
    
    print(result)
    df['TestResults'] = result 
        # now save the data frame
    writer = pd.ExcelWriter('D:\DriverResults.xlsx')
    df.to_excel(writer,'sheet1')
    writer.save()

    
def drivers():
    df['Driver Name'] = df['Driver Name'].str.replace(" ","")
    #print(df['Driver Name'])
    #print(type(df['Driver Name']))
    #print(str(df['Driver Name']))
    df['Driver Name'] = df['Driver Name'].str.lower()
    print(df['Driver Name'])
    
    
        
        
    d = subprocess.check_output([r'bat\CP1.bat'],shell=True).decode("utf-8")
    a = subprocess.check_output(['powershell.exe','-WindowStyle','hidden','Get-Wmiobject Win32_PnPSignedDriver|select DeviceName,DriverVersion'],shell=True).decode('utf-8')
    e = a + d
        #take input from sum and check in e
    finallist = e.replace(" ", "")
    finallist1 = finallist.lower()
    print(finallist1)
    sum = df['Driver Name'] + df['Version']
    print(sum)
    drivname = df['Driver Name']
    drivver = df['Version']
    def getresult(completestring):
        if completestring:
            completestring=completestring.group(0)
            return completestring
        else:
            return completestring 

    
    
        #sum is input from excel file
    #print(sum)
    #print(sum[0])
        #sum[6]="MicrosoftKernelDebugNetworkAdapter10.0.14393.0"
    mylistlength = len(sum)
    result=[]
    for i in range(0,mylistlength):
        if drivname[i] in finallist1:
            pattern = '.*'
            result2=drivname[i]+drivver[i]
            
            completestring = re.search(drivname[i]+pattern+drivver[i], finallist1)
            #result1=getresult(completestring)
            #result1=str(result1)
            print(completestring)
            if completestring or (result2 in finallist1):
                result.append("Pass")
            else:
                result.append("Fail")
        else:
            result.append("Driver not installed")
    print(result)
    df['TestResults'] = result 
        # now save the data frame
    writer = pd.ExcelWriter('D:\DriverResults.xlsx')
    df.to_excel(writer,'sheet1')
    writer.save() 


def on_closing():
    if messagebox.askokcancel("Exit","Are You Sure?"):
        app.destroy()
 
"""def Results(Pass,Fail):
    global Passed,Failed
    Passed = Pass
    Failed = Fail"""
    
def runActions(progress, status,cb,DevEnt):
    
    if os.path.exists("D:\log.txt"):
        os.remove("D:\log.txt")
    
    #functions = [Dupport, PowerPlan,start_batch2]
    functions = [Banner,Devicever,printtext,Netdhcp,IE,IEbrowsing,DevExclam,syserr,RecycleEmpty,Useracc,Perm,DisplayRes,Services,Duplicateports,Powercheck,Ethernet,Portsrange]#
    alist = range(17)
    Device = DevEnt.get()
    combobox1 = cb.get()
    
    if (len(combobox1) !=0) and (len(Device) !=0):
        if (combobox1.count(".") == 2) and (Device.count(".") == 1):
            try:
                p = 0
                Pass = 0
                Fail = 0
                #print("hello")
                for i in alist:
                    if i == 2:
                        Pass,Fail = functions[i](combobox1,Pass,Fail)
                        #print("hi")
                    elif i == 1:
                        Pass,Fail = functions[i](Device,Pass,Fail)
                    elif i ==0:
                        Pass,Fail = functions[i](Pass,Fail)
                    #elif i == 6:
                     #   functions[i]()
                        
                    else:
                        #print("sumanth")
                        Pass,Fail = functions[i](Pass,Fail)
                        #print("sumanth1")
                    #print("hai")
                    p += 1
                    unit = percentageCalculator(p, len(alist), case=2)
                #print(p)
                #print(len(alist))
                #TODO make a decorator!
                    time.sleep(1) #some func
                    step = "Working on {}".format(i) 
            #log.write(str('\n[OK]'))
                    progress['value'] = unit
                    percent['text'] = "{}%".format(int(unit))
                    status['text'] = "{}".format(step)
                    app.update()
                step="completed"
                status['text'] = "{}".format(step)
                #messagebox.showinfo('Info', "Process completed!")
                messagebox.showinfo("Process completed","PASS:{}\nFAIL:{}\n To check errors in test cases, follow the path: D:\log.txt".format(Pass, Fail))
                sys.exit()
            except Exception as e:
                messagebox.showinfo('Info', "ERROR: {}".format(e))
        
                sys.exit()
            
        else:
            #cb.delete(0, END)
            messagebox.showinfo("Warning!", "Please enter correct version")
    else:
            #TXE.delete(0, END)
        messagebox.showinfo("Warning!", "Box is empty! Write something")
    
 
class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        
        self.title("Sanity Test Cases Automation Tool")
        #self.minsize(600,400)
        self.wm_iconbitmap("mcd.ico")
 
 
        tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text = "Basic UI")
 
        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text = "Advanced UI")
        tabControl.pack(expand = 1, fill = "both")
        self.widgets()
    def fileDialog(self):
        global df
        filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("excel files","*.xlsx"),("all files","*.*")) )
        label = ttk.Label(labFrame, text = "")
        label.grid(column = 1, row = 2)
        label.configure(text = filename)
        df = pd.read_excel(filename)
        drivers()
        #all_data = pd.DataFrame(df)
        #print(all_data)
        #print(df['Driver Name'])
        
        
        
        
        
        #all_data = pd.DataFrame(df)
        

 
    def widgets(self):
        global percent,labelframe,labFrame
        
        labelFrame = LabelFrame(self.tab1, text = "Basic UI")
        labelFrame.grid(column = 0, row = 0)#, padx = 8, pady = 4


        labFrame = ttk.LabelFrame(labelFrame, text = "Test drivers")
        labFrame.grid(column = 0, row = 0, padx = 20, pady = 20)
        button = ttk.Button(labFrame, text = "Browse A File",command = self.fileDialog)
        button.grid(column = 1, row = 0)



        #row = Frame(labelFrame)
        Imagelab = Label(labelFrame, text="Enter image version",font="LARGE_FONT")
        #ImageVer = Entry(row)
        #row.pack(side=TOP, fill=X, padx=5, pady=5)
        Imagelab.grid(column = 0, row = 1,padx = 10,pady = 10)
        #ImageVer.pack(side=RIGHT, expand=YES, fill=X)
        data=["14.0.0", "12.3.0", "12.1.0"]
        #frame_name=Toplevel(win)
        cb=Combobox(labelFrame, values=data)
        cb.grid(column = 0, row = 2,padx = 10,pady = 10)
        Devlab = Label(labelFrame, text="Enter Device version",font="LARGE_FONT")#, width=20
        DevEnt = Entry(labelFrame)
        Devlab.grid(column = 0, row = 3,padx = 10,pady = 10)
        DevEnt.grid(column = 0, row = 4,padx = 10,pady = 10)
        #IElab = Label(labelFrame, text="Enter IE version",font="LARGE_FONT")
        #IEEnt = Entry(labelFrame)
        #IElab.grid(column = 0, row = 4,padx = 10,pady = 10)
        #IEEnt.grid(column = 0, row = 5,padx = 10,pady = 10)


 
        runButton = Button(labelFrame, text='Run TestCases',font="LARGE_FONT", command=(lambda : runActions(progress,status,cb,DevEnt)))#e=ents:
        percent = Label(labelFrame, text="", anchor=S) 
        progress = Progressbar(labelFrame, length=500, mode='determinate')    
        status = Label(labelFrame, text="Click button to start process..",width=80, relief=SUNKEN, anchor=W, bd=2) 
        runButton.grid(column = 0, row = 6,padx = 10,pady = 10)
        percent.grid(column = 0, row = 7,padx = 10,pady = 10)
        progress.grid(column = 0, row = 8,padx = 10,pady = 10)
        status.grid(column = 0, row = 9,padx = 10,pady = 10)

        labelframe = LabelFrame(self.tab2, text = "Advance UI")
        labelframe.grid(column = 0, row = 0, padx = 8, pady = 4)
        ADVANCEGUI(labelframe)
        """label = Label(labelFrame2, text="Enter Your Name:")
        label.grid(column=0, row=0, sticky='W')
        textEdit = Entry(labelFrame2, width=20)
        textEdit.grid(column=1, row=0)
        label2 = Label(labelFrame2, text="Enter Your Password:")
        label2.grid(column=0, row=1)
        textEdit = Entry(labelFrame2, width=20)
        textEdit.grid(column=1, row=1)"""


 
 
app = App() 

app.protocol("WM_DELETE_WINDOW",on_closing) 
 
 
 
 

app.mainloop()
