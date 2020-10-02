import subprocess
import re
#from Tabcontrolmain import Results


def DevExclam(Pass,Fail):
       log = open("D:\log.txt", "a")
       a = subprocess.check_output(['powershell.exe','Get-WmiObject Win32_PNPEntity | Where-Object{$_.ConfigManagerErrorCode -ne 0} | Select Name, DeviceID'],shell=True) 
       a = a.decode("utf-8")
       b = a.replace(" ","")
       c = b.replace("NameDeviceID","")
       d = c.replace("-","")
       if(not d.strip()): 
           #messagebox.showinfo("Result","passed")
           log.write(str('\n[7.Exclamation Mark: PASS]'))
           Pass+=1
       else :
           #messagebox.showerror("Result", "Failed")
           log.write(str('\n[7.Exclamation Mark: FAIL]'))
           Fail+=1
       return Pass,Fail
       log.close()
def Devicever(Device,Pass,Fail):
       log = open("D:\log.txt", "a")
       decimal = Device.split(".")
       d = subprocess.check_output([r'bat\Dp.bat'],shell=True).decode("utf-8")
       d = d.replace(" ","")
       f = d.split("REG_DWORD")
       hexlist = [hex(int(x)) for x in decimal]
       if (hexlist[0] in f[1][:3]) and (hexlist[1] in f[2][:3]):
                #messagebox.showinfo("Result","passed")
           log.write(str('\n[2.Device Version: PASS]'))
           Pass+=1
       else:
                #messagebox.showerror("Result","failed")
           log.write(str('\n[2.Device Version: FAIL]'))
           Fail+=1
       return Pass,Fail
       log.close()
       

    
    
    
    
    
    
            
            
def DisplayRes(Pass,Fail):
       log = open("D:\log.txt", "a")
       
       a = subprocess.check_output(['powershell.exe','Get-WmiObject -class "Win32_DisplayConfiguration" | select PelsHeight,PelsWidth'],shell=True) 
       #subprocess.call(['powershell.exe','Get-WmiObject -class "Win32_DisplayConfiguration" | select PelsHeight,PelsWidth']) 

       a = a.decode("utf-8")
       #print(a)
       b = a.replace(" ", "")
       #print(b)
       if "7681024" in b:
           #messagebox.showinfo("Result","passed")
           log.write(str('\n[16.DisplayResolution: PASS]'))
           Pass+=1
       else:
           #messagebox.showerror("Result","Failed")
           log.write(str('\n[16.DisplayResolution: FAIL]'))
           Fail+=1
       return Pass,Fail
       log.close()
def Duplicateports(Pass,Fail):
       log = open("D:\log.txt", "a")
       #print("DUPP")
       
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a= subprocess.check_output(['powershell.exe','-WindowStyle ','hidden','-command','Get-WmiObject Win32_SerialPort | Select-Object deviceid '])
       #a= subprocess.check_output(['powershell.exe','-nologo','Get-WmiObject Win32_SerialPort | Select-Object deviceid '])
       Dupres= subprocess.check_output(['powershell.exe','Get-WmiObject Win32_SerialPort | Select-Object deviceid '],shell=True)
       
       DupDec = Dupres.decode("utf-8")
       #print(a)
       words = Dupres.split()
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
           log.write(str('\n[20.DuplicatePorts: PASS]'))
           Pass+=1
       else:
           log.write(str('\n[20.DuplicatePorts: FAIL]'))
           Fail+=1
       #print("ENDDUP")
       return Pass,Fail
       log.close()
def Ethernet(Pass,Fail):
       log = open("D:\log.txt", "a")
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       a= subprocess.check_output(['powershell.exe', 'Get-NetIPConfiguration | select InterfaceAlias'],shell=True)      
       a = a.decode("utf-8")
       Replac = a.replace("InterfaceAlias","")
       Replace1 = Replac.replace("-","")
       Replace2 = Replace1.replace(" ","")
       #print(Replace2)
       list = Replace2.split()
       #print(list)
       checkstrings=['Ethernet','Ethernet2']
       #list1=['Ethernet','rh','jsdg']
       count = 0
       if len(list) > 2:
           #print("Fail")
           #messagebox.showerror("Result","Failed")
           log.write(str('\n[27.Ethernet: FAIL]'))
           Fail+=1
       elif len(list) ==2 :
           for lis in checkstrings:
               if lis in Replace2:
                   count +=1
               else:
                   #messagebox.showerror("Result", "Failed")
                   log.write(str('\n[27.Ethernet: FAIL]'))
                   Fail+=1

           
       else:
           if "Ethernet" in list:
               log.write(str('\n[27.Ethernet: PASS]'))
               Pass+=1
               #print("pass")
               #messagebox.showinfo("Result","passed")
           else:
               #messagebox.showerror("Result", "Failed")
               log.write(str('\n[27.Ethernet: FAIL]'))
               Fail+=1
       if count ==2:
           #print("pass")
           #messagebox.showinfo("Result","Passed")
           log.write(str('\n[27.Ethernet: PASS]'))
           Pass+=1
       return Pass,Fail
       log.close()
       
def IEbrowsing(Pass,Fail):
       log = open("D:\log.txt", "a")
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'ipconfig /all'])
       a = subprocess.check_output([r'bat\IEbrow.bat'],shell=True)
       #a = subprocess.check_output([r'powershell\Untitled3.ps1'])
       #a = subprocess.check_output(['powershell.exe','Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=TRUE -ComputerName']) 
       
       b = a.decode("utf-8")
       c = b.replace(" ","")
       #print(c)
       
       
       
       
       if "CouldnotdisplaytheDNSResolverCache." in c:
           #messagebox.showinfo("Result","passed")
           log.write(str('\n[6.Browsing History: PASS]'))
           Pass+=1
       else:
           #messagebox.showerror("Result", "Failed")
           log.write(str('\n[6.Browsing History: FAIL]'))
           Fail+=1
       return Pass,Fail
       log.close()
def Netdhcp(Pass,Fail):
       log = open("D:\log.txt", "a")
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'ipconfig /all'])
       a = subprocess.check_output([r'bat\Dhcp.bat'],shell=True)
       #a = subprocess.check_output(['powershell.exe','Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=TRUE -ComputerName']) 
       #print(a)
       a = a.decode("utf-8")
       #print(a)
       s = a.replace(". ", "")
       p = s.replace(": ", "")
       
       #print(p)
       if "DHCP EnabledYes" in p:
           #messagebox.showinfo("Result","passed")
           log.write(str('\n[4.Dhcp: PASS]'))
           Pass+=1
       else:
           #messagebox.showerror("Result", "Failed")
           log.write(str('\n[4.Dhcp: FAIL]'))
           Fail+=1
       return Pass,Fail
       log.close()
def OpenReg():
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'regedit'])
       subprocess.call([r'bat\Reg.bat'],shell=True)
def Perm(Pass,Fail):
       log = open("D:\log.txt", "a")
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'ipconfig /all'])
       #a = subprocess.check_output([r'bat\PM.bat'])
       #a = subprocess.check_output([r'bat\IE.bat'])
       a = subprocess.check_output(['powershell.exe','-WindowStyle ','hidden','Get-Acl C: | select AccessToString | fl;Get-Acl D: | select AccessToString | fl;Get-Acl E: | select AccessToString | fl'],shell=True) 
       
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
                         #else:
                                #messagebox.showerror("Result","Failed")
                                #log.write(str('\n[14.Permissions: FAIL]'))
                                
                                
                     else:
                            counter+=1
                            
       if counter1 == 0 and counter == 12:     
              #messagebox.showinfo("Result","passed")
              log.write(str('\n[14.Permissions: PASS]'))
              Pass+=1
       else:
              #messagebox.showerror("Result","Failed")
              log.write(str('\n[14.Permissions: FAIL]'))
              Fail+=1
       return Pass,Fail
       log.close()
def Powercheck(Pass,Fail):
       log = open("D:\log.txt", "a")
       print("startPowerplan")
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a= subprocess.check_output(['powershell.exe','-WindowStyle ','hidden','-command', 'powercfg -list '])
       #a= subprocess.check_output(['powershell.exe','-nologo', 'powercfg -list '])
       PowerPlanRes= subprocess.check_output(['powershell.exe','-WindowStyle ','hidden', 'powercfg -list '],shell=True)
       
       PowerPlanRes = PowerPlanRes.decode("utf-8")
       #print(a)
       PowerPlanRep = PowerPlanRes.replace(" ","")
       
       #print(b)
       if "(McDonald'sPowerPlan)*" in PowerPlanRep:
              #messagebox.showinfo("Result","passed")
           log.write(str('\n[26.powerplan: PASS]'))
           Pass+=1
              
       else:
              #messagebox.showerror("Result", "Failed")
           log.write(str('\n[26.powerplan: FAIL]'))
           Fail+=1
       print("EndPowerplan")
       return Pass,Fail
       log.close()
def Qfepatch():
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'wmic qfe list']).decode("utf-8")
       #a = subprocess.check_output([r'bat\qfe.bat']).decode("utf-8")
       subprocess.call([r'bat\qfe.bat'],shell=True)
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

def Banner(Pass,Fail):
   # global Passed,Failed
    #Passed = Pass
   # Failed = Fail
    #Fail=0
    log = open("D:\log.txt", "a")
    RC = subprocess.check_output([r'bat\RC.bat'],shell=True).decode("utf-8")
       #print(RC)
    if "Release Candidate" in RC:
        log.write(str('\n[1.RCbanner: FAIL]'))
        Fail+=1
    else:
        log.write(str('\n[1.RCbanner: PASS]'))
        Pass+=1
    return Pass,Fail
    log.close()
       



def Kms():
       a = subprocess.check_output([r'bat\Kms.bat'],shell=True).decode("utf-8")
       #a = subprocess.check_output(['powershell.exe','Get-Acl C: | select AccessToString | fl;Get-Acl D: | select AccessToString | fl;Get-Acl E: | select AccessToString | fl']) 
       #print(a)

def Tabcal():
       #a = subprocess.check_output([r'bat\tab.bat']).decode("utf-8")
       subprocess.call([r'bat\tab.bat'],shell=True)
       #a = subprocess.check_output(['powershell.exe','Get-Acl C: | select AccessToString | fl;Get-Acl D: | select AccessToString | fl;Get-Acl E: | select AccessToString | fl']) 
       

def Portsrange(Pass,Fail):
       log = open("D:\log.txt", "a")
       port = subprocess.check_output([r'bat\Ports.bat'],shell=True).decode("utf-8")
       #a = subprocess.check_output(['powershell.exe','Get-Acl C: | select AccessToString | fl;Get-Acl D: | select AccessToString | fl;Get-Acl E: | select AccessToString | fl']) 
       #print(a)
       #port = "hai 5001-5150"
       if "5001-5150" in port:
           #messagebox.showinfo("Result","passed")
           log.write(str('\n[29.PortsRange: PASS]'))
           Pass+=1
       else:
           #messagebox.showerror("Result", "Failed")
           log.write(str('\n[29.PortsRange: FAIL]'))
           Fail+=1
       return Pass,Fail
       log.close()
def RecycleEmpty(Pass,Fail):
       log = open("D:\log.txt", "a")
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       #a = subprocess.check_output(['cmd.exe', 'ipconfig /all'])
       #a = subprocess.check_output([r'bat\IEbrow.bat'])
       a = subprocess.check_output(['powershell.exe','-WindowStyle ','hidden','(New-Object -ComObject Shell.Application).NameSpace(0x0a).Items() | Select-Object Name,Size,Path'],shell=True) 
       
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
           #messagebox.showinfo("Result","passed")
           log.write(str('\n[10.RecycleBin: PASS]'))
           Pass+=1
       else :
           #messagebox.showerror("Result", "Failed")
           log.write(str('\n[10.RecycleBin: FAIL]'))
           Fail+=1
       return Pass,Fail
       log.close()
def Services(Pass,Fail):
        log = open("D:\log.txt", "a")
        a= subprocess.check_output(['powershell.exe','-WindowStyle ','hidden', 'get-service UI0Detect | select Displayname,Status,ServiceName,Can*;Get-Service UI0Detect | select -property name,starttype;get-service Spooler | select Displayname,Status,ServiceName,Can*;Get-Service Spooler | select -property name,starttype;Get-Service W32Time | select -property name,starttype;Get-Service wuauserv | select -property name,starttype;Get-Service MpsSvc | select -property name,starttype;get-service MpsSvc | select Displayname,Status,ServiceName,Can*;Get-NetFirewallProfile -All'],shell=True).decode("utf-8")
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
               
            #messagebox.showinfo("Result","passed")
            log.write(str('\n[18.Services: PASS]'))
            Pass+=1
        else:
            #messagebox.showerror("Result", "Failed")
            log.write(str('\n[18.Services: FAIL]'))
            Fail+=1
        return Pass,Fail
        log.close()
        
def IE(Pass,Fail):
    log = open("D:\log.txt", "a")
    
   
    a = subprocess.check_output([r'bat\IE.bat'],shell=True)
    a = a.decode("utf-8")
    #print(a)
    regex = r"\.\d+"
        #print(regex)
    matches = re.findall(regex, a)
        #print(matches)
    converttostring = "".join(matches)
    matches1="11"+converttostring
    if matches1 in a:
            #messagebox.showinfo("Result","passed")
        log.write(str('\n[5.IEVersion: PASS]'))
        Pass+=1
    else:
            #messagebox.showerror("Result", "Failed")
        log.write(str('\n[5.IEVersion: FAIL]'))
        Fail+=1
    return Pass,Fail
    log.close()
        

   
def Useracc(Pass,Fail):
       log = open("D:\log.txt", "a")
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       a = subprocess.check_output(['powershell.exe','-WindowStyle ','hidden', 'net user'],shell=True)      
       a = a.decode("utf-8")
       #print(a)
       #s = a.replace(" ", "")
       #print(s)

       m = a.count("Administrator")
       #print(m)
       if m is 1:
           #messagebox.showinfo("Result","passed")
           log.write(str('\n[12.Useraccounts: PASS]'))
           Pass+=1
           
       else:
           #messagebox.showerror("Result", "Failed")
           log.write(str('\n[12.Useraccounts: FAIL]'))
           Fail+=1
       return Pass,Fail
       log.close()

def syserr(Pass,Fail):
       log = open("D:\log.txt", "a")
       #os.system('powershell.exe Get-EventLog -LogName System -EntryType Error')
       a= subprocess.check_output(['powershell.exe','-WindowStyle ','hidden', 'Get-EventLog -LogName System -EntryType Error'],shell=True)      
       a = a.decode("utf-8")
       #print(a)
       if "Error" in a:
           #messagebox.showerror("Result", "Failed")
           log.write(str('\n[8.SystemError: FAIL]'))
           Fail+=1
       else:
           #messagebox.showinfo("Result","passed")
           log.write(str('\n[8.SystemError: PASS]'))
           Pass+=1
       return Pass,Fail
       log.close()

def printtext(combobox1,Pass,Fail):
    global log
    log = open("D:\log.txt", "a")
    decimal = combobox1.split(".")
    d = subprocess.check_output([r'bat\IE3.bat'],shell=True).decode("utf-8")
    replace = d.replace(" ","")
    f = replace.split("REG_DWORD")
    hexlist = [hex(int(x)) for x in decimal]
    if (hexlist[0] in f[1][:3]) and (hexlist[1] in f[2][:3]) and (hexlist[2] in f[3][:3]):
        log.write(str('\n[3.ImageVersion: PASS]'))
        Pass+=1
    else:
        log.write(str('\n[3.ImageVersion: FAIL]'))
        Fail+=1
    return Pass,Fail
    log.close()
            

           

                  

