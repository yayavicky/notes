---
typora-root-url: Pickit3
---

## 如何用labview调用Pickit3烧录

labview调用命令行的方式来调用烧录器烧录，你安装的mplab里面应该也有相应的应用程序，PK3CMD.EXE 你找找看，图片是相关的一些命令


+ [Supporting Third Party Programming Tools - Flowcode Help](https://www.matrixtsl.com/wikiv7/index.php?title=Supporting_Third_Party_Programming_Tools#PICkit3_using_PK3CMD_.28OLD.29)

### 1. PICkit3 using PK3CMD (OLD)

There are two options for using the PICkit 3 depending on how you are powering your hardware:


**Powered externally**

Location:

```
$(appdir)tools\PICkit3\PK3CMD.exe
```

Parameters (8-bit PIC):

```
-P$(chip) -F$(target).hex -E -M
```


Parameters (16-bit PIC):

```
-P$(chip) -F$(target).hex -E -M -L
```


**Powered via the PICkit**

Location:

```
$(appdir)tools\PICkit3\PK3CMD.exe
```

Parameters (8-bit PIC):

```
-P$(chip) -F$(target).hex -V5 -E -M
```


Parameters (16-bit PIC):

```
-P$(chip) -F$(target).hex -V3.3 -E -M -L
```


Please note that the PICkit 3 will fail to program if you have spaces in your Flowcode project name, replacing spaces with underscores or removing them completely should resolve the issue.



Also note that if your using the PICkit 3 with MPLABX or have bought a new one recently then you will likely have to downgrade the firmware to allow Flowcode to work with the PICkit.

Full details on how to do this are available from [here](http://woodworkerb.com/pickit-3-and-flowcode-6/).



### 2. ICD3 using MPLABX IPE (NEW)

First make sure you have the latest MPLAB X installed on your computer. We used version 3.30 which is used in the location path shown below. Make sure your path matches your installed location.

There are two options for using the ICD3 depending on how you are powering your hardware:


**Powered externally**

Location:

```
C:\Program Files (x86)\Microchip\MPLABX\v3.30\mplab_ipe\ipecmd.exe
```

Parameters:

```
/P$(chip) /F"$(outdir)$(target).hex" /TPICD3 /M /OL
```


**Powered via the ICD3**

Location:

```
C:\Program Files (x86)\Microchip\MPLABX\v3.30\mplab_ipe\ipecmd.exe
```

Parameters - Powered at 3V3:

```
/P$(chip) /F"$(outdir)$(target).hex" /TPICD3 /M /OL /W3.3
```

Parameters - Powered at 5V:

```
/P$(chip) /F"$(outdir)$(target).hex" /TPICD3 /M /OL /W5
```



If your still having problems getting the PICkit 3 to fire up then this [forum topic](http://www.matrixtsl.com/mmforums/viewtopic.php?f=54&t=12970&p=58454#p52318) may be of help.



### 3. PICKit3 Error PK3Err0033

https://www.microchip.com/forums/m875939.aspx

Hi, I tried to program so PIC24FJ64GB002 processors using MPLab8 but it didn't work. I used the PICKit 3 v 3.10 and it work great, except at the end of each run I get PICKit3.ini access denied. The programmer works just fine now with 3.10 but when I go back to MPLab8 I get a PK3Err0033 error. What did I do wrong and is there a fix for the PICKit3. Thank you for any assistance.



## MPLAB® X Integrated Development Environment (IDE)

https://www.microchip.com/en-us/development-tools-tools-and-software/mplab-x-ide#tabs

## [IPECMD - Automate MPLAB X programming process using command line](https://microchipsupport.force.com/s/article/Automate-MPLAB-programming-process-using-command-lineIPECMD)



**Programming Tools Supported**

Refer to their respective readmes for additional information:

- MPLAB PICkit™ 4 in-circuit debugger/production programmer
- MPLAB Snap in-circuit debugger/development programmer
- PICkit 3 in-circuit debugger/development programmer
- MPLAB ICD 4 in-circuit debugger/production programmer
- MPLAB ICD 3 in-circuit debugger/production programmer
- MPLAB REAL ICE™ in-circuit emulator/production programmer
- MPLAB PM3 production programmer
- PICkit On Board (PKOB) demo boards
- PICkit On Board 4 (PKOB4) demo boards



```
@REM pushd %out_dir%
@REM rename  %org_dir_name% %tar_dir_name%
@REM popd
```







