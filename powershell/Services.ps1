get-service UI0Detect | select Displayname,Status,ServiceName,Can*
Get-Service UI0Detect | select -property name,starttype
get-service Spooler | select Displayname,Status,ServiceName,Can*
Get-Service Spooler | select -property name,starttype
Get-Service W32Time | select -property name,starttype
Get-Service wuauserv | select -property name,starttype
Get-Service MpsSvc | select -property name,starttype

