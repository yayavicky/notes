https://www.cnblogs.com/shouke/p/14288437.html



+ https://docs.python.org/3/library/logging.html
+ https://docs.python.org/3/howto/logging.html#logging-basic-tutorial



## logging.basicConfig() --日志配置的快速方法

支持将log输出到控制台（Console）或文件中，但只支持一种。

```py
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logging.info('this is info log')
```

basicConfig(**kwargs)代码长这个样子：

```py
root = RootLogger(WARNING)
Logger.root = root
Logger.manager = Manager(Logger.root)

def basicConfig(**kwargs):
    # Add thread safety in case someone mistakenly calls
    # basicConfig() from multiple threads
    _acquireLock()
    try:
        if len(root.handlers) == 0:
            filename = kwargs.get("filename")
            if filename:
                mode = kwargs.get("filemode", 'a')
                hdlr = FileHandler(filename, mode)
            else:
                stream = kwargs.get("stream")
                hdlr = StreamHandler(stream)
            fs = kwargs.get("format", BASIC_FORMAT)
            dfs = kwargs.get("datefmt", None)
            fmt = Formatter(fs, dfs)
            hdlr.setFormatter(fmt)
            root.addHandler(hdlr)
            level = kwargs.get("level")
            if level is not None:
                root.setLevel(level)
    finally:
        _releaseLock()

```

可以看到，是先根据传入的内容，创建了logger(root)，又创建了相应的handler（FileHandler和StreamHandler，前者输入log到文件，后者输入到console），并为已创建的的handler设置格式（hdlr.setFormatter(fmt)），然后将创建的handler加入到 logger中（root.addHandler(hdlr)），最后为logger设置日志级别（root.setLevel(level)）。
由上可见basicConfig()是将日志配置的一些方法封装了起来。

## 日志配置的一般方法（logger→handler）

下面的例子实现将log同时输出到Console和日志文件，思路参考basicConfig()：

```py
import logging

logger = logging.getLogger()
logger.setLevel('DEBUG')
BASIC_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)
chlr = logging.StreamHandler() # 输出到控制台的handler
chlr.setFormatter(formatter)
chlr.setLevel('INFO')  # 也可以不设置，不设置就默认用logger的level
fhlr = logging.FileHandler('example.log') # 输出到文件的handler
fhlr.setFormatter(formatter)
logger.addHandler(chlr)
logger.addHandler(fhlr)
logger.info('this is info')
logger.debug('this is debug')

```

### 错误信息打印

```py
import logging
 
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
 
# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
 
# FileHandler
file_handler = logging.FileHandler('result.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
 
# StreamHandler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
 
# Log
logger.info('Start')
logger.warning('Something maybe fail.')
try:
    result = 10 / 0
except Exception:
    logger.error('Faild to get result', exc_info=True)
logger.info('Finished')
```

