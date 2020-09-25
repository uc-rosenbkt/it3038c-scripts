function getIP {
    (Get-NetIPAddress -InterfaceAlias Ethernet0).IPv4Address
}

$IP = getIP

write-host("This machine's IP is $IP")
write-host("This machine's IP is {0}" -f $IP)

$HOSTNAME = "rosenbkt-win"

$Date = Get-Date

$Body = "This machine's IP is {0}." -f $IP + "User is {0}." -f $env:USERNAME + "Hostname is {0}." -f $HOSTNAME + "Powershell version is {0}." -f $HOST.Version + "Today's date is {0}." -f $Date 

write-host($Body)

Send-MailMessage -To "keithrosenberger22@gmail.com" -From "keithrosenberger22@gmail.com" -Subject "IT3038C Windows Sysinfo" -Body $BODY -SmtpServer "smtp.gmail.com" -port 587 -UseSSL -Credential (Get-Credential)
