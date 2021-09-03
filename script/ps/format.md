

```powershell
#Aliases 
Get-ChildItem | % {Write-host "$($_.fullName)"

#No Aliases
Get-ChildItem | ForEach-Object { Write-Host "$($_.FullName)"

```



## vs code

+ ` “File -> Preferences -> Settings” `
+ `Ctrl + ` powershell

> You must have Powershell extension installed



- PowerShell -> Code Formatting: Auto Correct Aliases
  - powershell.codeFormatting.autoCorrectAliases
- PowerShell -> Code Formatting: Use Correct Casing
  - powershell.codeFormatting.useCorrectCasing