---
typora-root-url: answer
---

# prepare

+ cn_windows_10_business_editions_version_21h1_updated_jun_2021_x64_dvd_9d9154fa.iso

+ ADK



## 文件设置

### 1. 复制 `F:\sources\install.wim`

### 2. 打开安装好的"**Windows System Image Mannager**",下面简称“**WIM**”

![image-20210823103047335](./windows_Kits)

![image-20210823103954203](./windows_Kits_2)



### 3. 使用“**WIM**”，选择“**install.wim**”

如果提示选择版本，选择自己需要的版本,我选择的专业版“Windows 10 Pro”
其他的就点“是”或“确定”

![在这里插入图片描述](./open_wim)

加载后的界面，如下

![在这里插入图片描述](/load_win)

### 4. 参数设置
下面我们将对自动应答文件参数进行设置

![在这里插入图片描述](/set_lan)

![在这里插入图片描述](./set_lan2)

![image-20210823112544053](./set_lan2)

+ “zh-CN”是中文的意思，您也可以设置别的语言, en-US 

  + [默认输入配置文件 (输入法区域设置) 在 Windows | Microsoft Docs](https://docs.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/default-input-locales-for-windows-language-packs)

  + `UILanguageFallback` specifies the language that is used for resources that are not localized for the default system user interface (UI) (the [UILanguage](https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-international-core-uilanguage) setting).

    This setting is used by Windows Setup and Windows Deployment Services.

    UILanguageFallback 应该设为 en-US

    + `SetupUILanguage` defines the language to use in Windows Setup and Windows Deployment Services.   `en-US`
    + `InputLocale` specifies the input language and method for input devices, such as the keyboard layout.  The input locale (also called input language) is a per-process setting that describes an input language (for example, Greek) and an input method (for example, the keyboard). `en-US`
    + `UserLocale` specifies the per-user settings used for formatting dates, times, currency, and numbers in a Windows installation.  `zh-CN`
    + `SystemLocale` specifies the default language to use for non-Unicode programs.   `zh-CN`
    + `UILanguage` specifies the default system language to display user interface items (such as menus, dialog boxes, and help files).   `zh-CN`
    + UILanguageFallback specifies the language to use for resources that are not localized for the default system user interface (UILanguage setting). `en-US`

+ “LayerDriver”是键盘种类

+ ![在这里插入图片描述](/set_lan_3)

+ “WillShowUI”表示安装之前是否显示对话框

+ “OnError”表示有错误时显示对话框

+ “Never”表示任何情况下都不显示

+ “Always”表示每次都显示

![在这里插入图片描述](/set_lan_4)

![在这里插入图片描述](/set_lan_5)

+ “EnableFirewall”设置PE启动防火墙
+ “EnableNetwork”设置PE启动网络
+ “Restart”设置安装完成后PE进行重启
+ “UseConfigurationSet”设置安装时会停下来寻找驱动

![在这里插入图片描述](./set_lan_6)

+ “ AcceptEula”设置跳过授权协议

  ![在这里插入图片描述](/set_lan_7)

+ “Key”设置安装版本，我是专业版所以一定是专业版秘钥，否则后面会出错

  `DNCGK-D8Q6V-VBDKC-TRPKY-R6YQB`

+ “WillShowUI”设置安装之前是否显示对话框

  ![img](./set_lan_8)

  ![在这里插入图片描述](./set_lan_09)

+ “SkipAutoActivation”设置跳过自动激活 Microsoft Windows 许可证



![在这里插入图片描述](./skip_auto_activation)

![在这里插入图片描述](/bluteooth)



+ “BluetoothTaskbarIconEnabled”设置指定蓝牙图标未显示在任务栏中
+ “DisableAutoDaylightTimeSet ”设置指定计算机上的时间使用标准时间
+ “RegisteredOrganization”设置定最终用户的组织名称
+ “RegisteredOwner”设置最终用户的名称
+ “ShowWindowsLive”设置隐藏ShowWindows Live
+ “TimeZone”设置计算机的时区为中国

窗口界面语言设置

![在这里插入图片描述](./ui_lan1)

![在这里插入图片描述](./ui_lan2)

+ “Enabled”设置指定是否启用自动登录过程
+ “LogonCount”设置指定帐户的使用次数
+ “Username”设置指定用于自动登录的用户帐户名，如果管理员登录设置为“Administrator”

![在这里插入图片描述](./password)

选择“Password”点击“Value”右键点击“写入空字符串”设置登录密码为空

![在这里插入图片描述](./password_2)

安装上面的做法，把“Administrator”管理员登录密码设置为空

![在这里插入图片描述](./account)

+ “HideEULAPage”设置隐藏Windows欢迎使用Microsoft软件许可条款页
+ “HideLocalAccountScreen”设置在OOBE期间隐藏管理员密码屏幕
+ “HideOEMRegistrationScreen”设置在OOBE期间隐藏的OEM注册页
+ “HideOnlineAccountScreens”设置在OOBE期间隐藏登录页
+ “HideWirelessSetupInOOBE”设置OOBE期间隐藏Windows欢迎屏幕
+ “NetworkLocation”设置网络为家庭网络，"Work"为工作网络
+ “ProtectYourPC”设置关闭快速设置，“2”是设置打开快速设置
+ “UnattendEnableRetailDemo”设置禁用零售演示模式下在设备上

上面就是一些基础参数的设置，这些已经可以使系统自动安装
系统安装结束后会以管理员身份运行

设置完成后，我们需要对我们的文件进行检验，查看是否有错误
检验结果会在右下角

没有错误，我们需要将文件保存下来
将文件保存为“Autounattend”的xml文件

以上就是我们创建的无人值守应答文件

