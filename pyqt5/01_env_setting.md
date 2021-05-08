
# python国内镜像源


+ 清华：https://pypi.tuna.tsinghua.edu.cn/simple
+ 阿里云：http://mirrors.aliyun.com/pypi/simple/
+ 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
+ 华中理工大学：http://pypi.hustunique.com/
+ 山东理工大学：http://pypi.sdutlinux.org/ 
+ 豆瓣：http://pypi.douban.com/simple/

>note：新版ubuntu要求使用https源，要注意。
 如：pip3 install -i https://pypi.doubanio.com/simple/ 包名

 
## 临时使用：

 可以在使用pip的时候加参数-i https://pypi.tuna.tsinghua.edu.cn/simple

 例如：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider，这样就会从清华这边的镜像去安装pyspider库。
 
 pip install ipython -i http://mirrors.aliyun.com/pypi/simple/
 pip install ipython -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

## 永久修改，一劳永逸：

### Linux下，

修改 ~/.pip/pip.conf (没有就创建一个文件夹及文件。文件夹要加“.”，表示是隐藏文件夹)

内容如下：

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

[install]
trusted-host=mirrors.aliyun.com
```

### windows下，

直接在user目录中创建一个pip目录，再新建文件pip.ini。（例如：C:\Users\WQP\pip\pip.ini）内容同上。

### Mac OS

```
~ mkdir .pip	# 在家目录下创建一个.pip目录
~ cd .pip
~ touch pip.conf # 创建一个pip配置文件
# 写入配置
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
```


