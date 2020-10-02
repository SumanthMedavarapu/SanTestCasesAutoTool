Get-Wmiobject Win32_PnPSignedDriver|select DeviceName,DriverVersion|where{$_.DeviceName -like "Volume Manager"}
