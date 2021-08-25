## 安装



```shell
pip install pipreqs
```

### 用法

```shell
pipreqs somedir/location

# 输出requirements.txt到项目根目录下
pipreqs --use-local ./
```
>错误1 UnicodeDecodeError

```shell
UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position XXX: illegal multibyte sequence
```

指定编码格式

```shell
# 输出requirements.txt到项目根目录下
pipreqs --encoding=utf8 --use-local ./
pipreqs --encoding=utf8  ./
```

>错误2

```shell
(EpdsRawEnv) D:\Remote\EpdsTestPlatform>pipreqs --encoding=utf8  ./
ERROR: Failed on file: ./ui\style.py
Traceback (most recent call last):
  File "c:\python\python37\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "c:\python\python37\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "C:\Python\Python37\Scripts\pipreqs.exe\__main__.py", line 7, in <module>
  File "c:\python\python37\lib\site-packages\pipreqs\pipreqs.py", line 470, in main
    init(args)
  File "c:\python\python37\lib\site-packages\pipreqs\pipreqs.py", line 409, in init
    follow_links=follow_links)
  File "c:\python\python37\lib\site-packages\pipreqs\pipreqs.py", line 138, in get_all_imports
    raise exc
  File "c:\python\python37\lib\site-packages\pipreqs\pipreqs.py", line 124, in get_all_imports
    tree = ast.parse(contents)
  File "c:\python\python37\lib\ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    ﻿# -*- coding: utf-8 -*-
    ^
SyntaxError: invalid character in identifier

```

BOM-symbol的问题

>什么是BOM？首先了解一下BOM，字节顺序标记（英语：byte-order mark，BOM）是位于码点U+FEFF的统一码字符的名称。当以UTF-16或UTF-32来将UCS/统一码字符所组成的字符串编码时，这个字符被用来标示其字节序。它常被用来当做标示文件是以UTF-8、UTF-16或UTF-32编码的记号。【来自维基百科】。



通过读文件的方式，利用`ord()`函数，读到`.py`文件的开头不可见字符的Unicode编码是`65279`，然后就简单写了一个脚本，利用该脚本将文件中的`chr(65279)`字符删除。为了方便以后使用，写的脚本是基于命令行的，如下：

```python
import os
import sys

ProjectDir = os.path.abspath(os.path.pardir)

FILE_LIST = []
file_ends = ['.py', ]

def replace_remove_65279(file_path):
    print("will replace: ", file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(file_path, 'w', encoding='utf-8') as ff:
        for line in lines:
            line = line.replace(chr(65279), '')
            ff.write(line)


def walk_dir(tar_dir, topdown=True):
    for root, dirs, files in os.walk(tar_dir, topdown):
        for name in files:
            for item in file_ends:
                if name.lower().endswith(item):
                    FILE_LIST.append(os.path.join(root, name))


walk_dir(ProjectDir)


for item in FILE_LIST:
    replace_remove_65279(item)

```

