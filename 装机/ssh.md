## UI

1. 在开始图标右键，选择应用和功能，弹出如下设置界面，点击管理可选功能
2. 选择管理可用功能，弹出管理可选功能，点击添加功能
3. 在弹出的添加功能中选择 OpenSSH 客户端
4. 安装成功后返回即可看到

## command

```powershell
Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'

# This should return the following output:

Name  : OpenSSH.Client~~~~0.0.1.0
State : NotPresent
Name  : OpenSSH.Server~~~~0.0.1.0
State : NotPresent

# Install the OpenSSH Client
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Install the OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Both of these should return the following output:

Path          :
Online        : True
RestartNeeded : False
```

## enter

```shell
ssh user@ip -p port 
```

## 乱码



```shell
cat 加大电子科技无锡有限公司_20210825.ADF.sha256  | iconv -f GBK -t utf-8
```



```powershell
PS C:\Windows\system32>  netsh firewall set icmpsetting 8

重要信息: 已成功执行命令。
但是，"netsh firewall" 已弃用；
请改用 "netsh advfirewall firewall" 。
有关使用 "netsh advfirewall firewall" 命令
而非 "netsh firewall" 的详细信息，请参阅
 https://go.microsoft.com/fwlink/?linkid=121488 上的 KB 文章 947709。

确定。

```

