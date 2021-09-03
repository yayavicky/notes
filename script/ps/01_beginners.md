+ https://powershell.org/
+ https://www.youtube.com/watch?v=UVUd9_k9C6A



## common command

1. `set-location`
2. `get-childitem`

3. `clear-host`
4. `cd\`
5. `get-alias`  - `gal`
   1. `gal pwd`
   2. `gal g*`
   3. `get-alias -Definition get-process`
6.  `ipconfig /all`
7. service
   1. `gsv` - `get-service`
   2. `sasv` - `start-service`
   3. `spsv` - `stop-service`

## Help

1. `update-help`
   1. `update-help -Force`
2. `get-help`
   1. `get-help get-service`
   2. `help get-service`
   3. `man get-service`
3. `get-help *service*`
   1. `get-help g*service*`
   2. `get-help get-service -detailed`
   3. `get-help get-service -examples`
   4. `get-help get-service -full`
   5. `get-help get-service -online`
   6. `get-help get-service -showwindow`
4. `get-verb | measure`
5. `get-help *eventlog*`



+ `get-service vmi*`
+ `get-service -displayname *network*`
+ `get-service -Name bits, bfe`

## pipeline

`get-service | select-object name, status | sort-object name`

```shell
get-service -name bits
stop-service -name bits
get-service -name bits | stop-service
get-service -name bits | start-service -passthru
get-service | export-csv -Path d:\test\service.csv
import-csv d:\test\service.csv

get-service | export-clixml -Path d:\test\service.xml
```

compare examples

```shell
get-process | export-clixml -Path d:\test\good.xml

notepad
calc
compare-object -ReferenceObject (import-clixml d:\test\good.xml) -DifferenceObject (get-process) -Property name
```

out put

```shell
get-service | out-file -filepath d:\test\somefile.txt
get-content d:\test\somefile.txt
```

convert

```shell
get-service |  ConvertTo-Csv 

get-service |  ConvertTo-html -property name, status | out-file d:\test\services.html
```

whatif

```shell
stop-service bits -whatif
stop-service bits -confirm
```

## Extending the shell

`mmc`

```shell
# currently loaded module
Get-Module

Get-Module -ListAvailable
```

## Object for the Admin

```shell
get-process | where Handles -gt 900
get-process | where Handles -gt 900 | sort Handles

Get-Service -name bits | Get-Member
Get-Service -name bits | gm

Get-ChildItem | select -Property name, length | sort length
Get-ChildItem | select -Property name, length | sort -Property length
Get-ChildItem | select -Property name, length | sort length -Descending

Get-EventLog -LogName System -Newest 5 | gm

Get-EventLog -LogName System -Newest 5 | select -Property EventID, TimeWritten, Message
```

### practice

```shell
$x =[xml](cat D:\test\service.xml)
$x.GetType()

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
True     False    XmlDocument                              System.Xml.XmlNode

$x.Objs.Obj

RefId    : 2746
TNRef    : TNRef
ToString : XblAuthManager
Props    : Props
MS       : MS

RefId    : 2757
TNRef    : TNRef
ToString : XblGameSave
Props    : Props
MS       : MS

RefId    : 2769
TNRef    : TNRef
ToString : XboxGipSvc
Props    : Props
MS       : MS

RefId    : 2775
TNRef    : TNRef
ToString : XboxNetApiSvc
Props    : Props
MS       : MS
```

```shell
 $x.Objs.Obj[10]

RefId    : 92
TNRef    : TNRef
ToString : aspnet_state
Props    : Props
MS       : MS
```

```shell
Get-History

# v2
Get-Service | where {$_.status -eq "running"}

# from V3
Get-Service | where {$PSItem.status -eq "running"}

Get-Service | where {$PSItem.status -eq "running" -and $_.name -like "b*"}
```

```shell
get-process | where {$_.handles -gt 1000}
get-process | where handles -gt 1000
```

## deep in pipeline

how pipeline work

1. by value
2. by property name
3. what if property doesn't work, customize it
4. the parenthetical - when all else fail

```shell
calc
get-process Calculator | dir


    目录: C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_10.2103.8.0_x64__8wekyb3d8bbwe


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          2021/5/7     10:35        5013504 Calculator.exe

```

服务器

```shell
get-adcomputer

# hack
get-adcomputer -filter * | select -Property name, @{name='ComputerName';expression={$_.name}}
get-adcomputer -filter * | select -Property name, @{n='ComputerName';e={$_.name}}
get-adcomputer -filter * | select -Property name, @{label='ComputerName';e={$_.name}}
get-adcomputer -filter * | select -Property name, @{l='ComputerName';e={$_.name}}

get-adcomputer -filter * | select -Property @{l='ComputerName';e={$_.name}}

get-adcomputer -filter * | select -Property @{l='ComputerName';e={$_.name}} | get-service -name bits
```

BIOS

```shell
Get-WmiObject -Class win32_bios

SMBIOSBIOSVersion : RMRCM400P0904
Manufacturer      : TIMI
Name              : RMRCM400P0904
SerialNumber      : 28596/00005150
Version           : XMCC - 2

Get-WmiObject -Class win32_bios -ComputerName  XXX,XXX,xxx
# V2
Get-WmiObject -Class win32_bios -ComputerName  (get-adcomputer -filter * | select -ExpandProperty name)
# V3
Get-WmiObject -Class win32_bios -ComputerName  (get-adcomputer -filter *).name

# not work
get-adcomputer -filter * | Get-WmiObject -Class win32_bios
# work
get-adcomputer -filter * | Get-WmiObject -Class win32_bios -ComputerName {$_.Name}


# new
Get-CimInstance 
# old
Get-WmiObject

Get-CimInstance  -Class win32_bios
```

## Remoting

```shell
Enter-PSSession server1

Enable-PSRemoting
# 由于此计算机上的网络连接类型之一设置为公用，因此 WinRM 防火墙例外将不运行。 将网络连接类型更改为域或专用，然后再次尝试。

```

+ Group Policy Management Editor
+ Windows Remote Management(WinRM)
+ WinRM Service - enable

```shell
Enter-PSSession -ComputerName server1

Get-EventLog -LogName System -New 3

# not remoting
Invoke-Command -ComputerName XX {Get-EventLog -LogName System -New 3}
```

only server

```shell
Get-Windowsfeature
Install-WindowsFeature windowspowershellwebAccess

get-help *pswa*

```

trick 仅演示

web 访问

```shell
Add-PswaAuthorizationRule * * *

#退出机器
start iexplore https://pwa/pswa
```

remoting 传递对象，有利于pipeline 进一步处理

```shell
invoke-command -ComputerName cc,xx,aa {Get-EventLog -LogName System -Newest 3} | sort timewritten | format-table -Property timewritten, message -AutoSize

invoke-command
icm
```



```shell
icm xx,xxx {Get-Volume} | sort SizeRemaining
```

## Automation

+ security goals
+ Execution Policy
+ Variables: a place to store stuff
+ Fun with Quotes
+ Getting and displaying input
+ Other output for scripts and automation

### 1. security goal

+ secured by default
+ prevents mistakes by unintentional admins and users
+ no script execution
+ .ps1 associated with notepad
+ must type path to execute a script

### 2. Execution Policy

+ by default, powershell does not run scripts
+ get/set-executionpolicy
+ restricted
+ unrestricted
+ allsigned
+ remoteSigned
+ bypass
+ undefined
+ can be set with group policy



```shell
New-SelfSignedCertificate

Get-PSDrive

dir cert:\
dir Cert:\CurrentUser
dir Cert:\CurrentUser -Recurse
dir Cert:\CurrentUser -Recurse -CodeSigningCert
dir Cert:\CurrentUser -Recurse -CodeSigningCert -OutVariable a
$a
$cert = $a[0]

Get-ExecutionPolicy
RemoteSigned

Set-ExecutionPolicy AllSigned

Set-AuthenticodeSignature -Certificate $cert -FilePath .\test.ps1
```

变量

```shell
$myvar = get-service bits
$myvar.status
Stopped

$myvar.start()
$myvar.status
Stopped

$myvar.refresh()
$myvar.status
Running
```

```shell
$var = read-host "enter a computer name"

write-host $var -ForegroundColor red -BackgroundColor green
```

> write-host 不会给pipeline 输入
>
> write-output 可以给pipeline输入

```shell
write-warning "please don't do it!"
write-error "please don't do it!"
```

```shell
${ this is a test } = 4
${ this is a test }
4

1..5
1
2
3
4
5

${some file path}
```



## Automation in scale - remoting

```shell
$session = New-PSSession -ComputerName dc
Get-PSSession

icm -Session $sessions {$var=2}
icm -Session $sessions {$var}

measure-command {icm -ComputerName dc {Get-Process}}

```



```shell
$servers = 's1', 's2'

$servers | foreach{start iexplorer http://$_}

$s = New-PSSession -ComputerName $servers

icm -Session $s {Install-windowsFeature web-server}
$servers | foreach{start iexplorer http://$_}

$servers | foreach {copy-item d:\default.html -Destination \\$_\c$\inetpub\wwwroot}
$servers | foreach{start iexplorer http://$_}

```

```shell
$s = New-PSSession -ComputerName dc
# something like proxy
Import-PSSession -Session $s -Module ActiveDirectory -Prefix remote

Get-RemoteADComputer -filter *
```

## Tools

ISE

```shell
Get-WmiObject win32_logicaldisk 
Get-WmiObject win32_logicaldisk -Filter "DeviceId='C:'"

# Ctrl+Space 联想
Get-CimInstance Win32_LogicalDisk

Get-WmiObject win32_logicaldisk -Filter "DeviceId='C:'"| select @{n='freegb';e={$_.freespace /1gb}}

Get-WmiObject win32_logicaldisk -Filter "DeviceId='C:'"| select @{n='freegb';e={$_.freespace /1gb -as [int]}}
```

```powershell
<#
.Synopsis
short Explation
.Description
long Explation
.Parameter ComputerName
for remote computer
.Example
abc -computername remote
this is for a remote computer
#>
[CmdletBinding()]
param(
	[Parameter(Mandatory=$True)]
	[string]$ComputerName='localhost'
)
Get-WmiObject -computername $ComputerName -class win32_logicaldisk -Filter "DeviceId='C:'"
```

ISE 环境 `Ctl+J`

```powershell
function Get-abc{
	[CmdletBinding()]
	param(
		[Parameter(Mandatory=$True)]
	[string]$ComputerName='localhost'
	)
	Get-WmiObject -computername $ComputerName -class win32_logicaldisk -Filter "DeviceId='C:'"
}
```

```powershell
# load script
. .\scriptpath.ps1

-OutVariable $somevar
```

### module

+ `filename.psm1`

```powershell
Import-Module .\filename.psm1
Import-Module .\filename.psm1 -Force -Verbose
```

系统路径

```powershell
cat Env:\PSModulePath

$env:PSModulePath

$env:PSModulePath -split ";"
D:\vicky\Documents\WindowsPowerShell\Modules
C:\Program Files\WindowsPowerShell\Modules
C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules
C:\Program Files\WindowsPowerShell\Modules\
C:\Program Files (x86)\Microsoft SDKs\Azure\PowerShell\ResourceManager\AzureResourceManager\
C:\Program Files (x86)\Microsoft SDKs\Azure\PowerShell\ServiceManagement\
C:\Program Files (x86)\Microsoft SDKs\Azure\PowerShell\Storage\

# 用户路径
D:\vicky\Documents\WindowsPowerShell\Modules
# 系统路径
C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules
```

```powershell
Import-Module diskinfo
Remove-Module diskinfo
```



