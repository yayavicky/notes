[ShellHacks - Command-Line Tips and Tricks](https://www.shellhacks.com/)



```shell
certUtil -hashfile <PATH_TO_FILE> <HASH_ALGORITHM>
certUtil -hashfile C:\file.img MD5
certUtil -hashfile C:\file.img SHA256

# Windows CMD:
C:\> CertUtil -hashfile C:\file.img MD5 | findstr /v "hash"

# Windows PowerShell:
PS C:\> $(CertUtil -hashfile C:\file.img MD5)[1] -replace " ",""
```

Available hash algorithms:

```
MD2 MD4 MD5 SHA1 SHA256 SHA384 SHA512
```

Get help:

```
C:\> certutil -hashfile -?
```

