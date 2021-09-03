C:\Windows\servicing\TrustedInstaller.exe



右键，属性, 安全, 编辑, TrustedInstaller，下面把完全控制打勾。



管理员权限运行powershell

```powershell
# 下载
Save-Module -Name NtObjectManager -Path c:\token
Y
# 
Install-Module -Name NtObjectManager
A

Set-ExecutionPolicy Unrestricted

# 导入 NtObjectManager 模块
Import-Module NtObjectManager
```



## 开始正式获得 Trustedinstaller 权限

```powershell
sc.exe startTrustedInstaller
Set-NtTokenPrivilege SeDebugPrivilege
$p=Get-NtProcess -Name TrustedInstaller.exe
$proc=New-Win32Process cmd.exe -CreationFlags NewConsole -ParentProcess $p
```



接下来系统会打开一个命令提示符，该命令提示符就具有 Trustedinstaller 权限，可以直接修改系统文件。我们可以通过：



```powershell
whoami /groups /fo list
```

可以看到我们已经获得 Trustedinstaller 权限了，现在就可以通过一些命令修改系统文件了。如果想要更加方便操作，可以通过此 CMD 运行 taskmgr、notepad 等应用，在运行新任务、打开文件的浏览窗口下，进行文件编辑。编辑结束后直接关闭即可。

> 不要使用 CMD 运行 explorer，因为 explorer 无法在当前用户下正常使用。在这之后如果，想要重新获得 Trustedinstaller 权限重新执行以下命令即可：
>
> ```powershell
> sc.exe startTrustedInstaller
> Set-NtTokenPrivilege SeDebugPrivilege
> $p=Get-NtProcess -Name TrustedInstaller.exe
> $proc=New-Win32Process cmd.exe -CreationFlags NewConsole -ParentProcess $p
> ```
>
> 

