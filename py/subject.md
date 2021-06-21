
+ [异步 PEP-3156](https://www.python.org/dev/peps/pep-3156/)
+ [Awesome Asyncio](https://www.jianshu.com/p/4f667ecae64f)


## PEP

就像读Python标准库源代码一样，我也选择了阅读PEP来更了解Python。

PEP是Python Enhancement Proposals的缩写，翻译过来就是「Python增强建议书」。每个PEP文件可能是描述某新功能（比如asyncio模块）、信息（就是指导方针、共识等内容，比如Python之禅、Python新版本发布的时间表等）或者进程（Python开发中使用的工具、流程或者环境的更改，比如要迁移到Github，之前还提出迁到Gitlab但是被拒绝了）等。大部分情况下你可以把它当成设计文档，里面包含了技术规范和功能的基本原理说明等。

小插曲：IPython也有自己的增强建议书（Jupyter的在这里），在你的公司或者团队同样也可以有自己的EP，在豆瓣东西时我们就有自己的EPEP

全部的PEP可以在 PEP 0 -- Index of Python Enhancement Proposals (PEPs) 找到。PEP很有多类型，为了把时间花在刀刃上，也不需要所有的PEP文件都读，比如Rejected、Deferred、Superseded和Draft的。另外有些和我们学习使用Python关系不大，如新版本发布安排的，迁移项目托管平台的。每个PEP都有对应的类型（可以翻到最下面的Key小节看说明)，A R D S P甚至I基本不需要看。

除了PEP8，根据我的经验给大家列一些应该（值得）阅读的：

1. PEP 333 -- Python Web Server Gateway Interface v1.0 描述WSGI协议，告诉你如何在web服务器与web应用/web框架之间的可移植的标准接口。Web开发或者你想写Web框架必看。
2. PEP 3333 -- Python Web Server Gateway Interface v1.0.1 这是更新版的PEP 333，提高了Python 3的可用性。
3. PEP 484 -- Type Hints 类型约束
4. PEP 205 -- Weak References 以前一直对weakref模块不能理解，网上也找不到什么好的说明，这篇PEP会对你有帮助的
5. PEP 0282  https://www.python.org/dev/peps/pep-0282/ 虽然logging模块的官方文档已经很全面了，不过这篇PEP还是给我新的灵感了。比如我在3年前的电影时光网的爬虫中用到的 makeLogRecord 最初就是看这篇PEP想到的。
6. PEP 309 -- Partial Function Application 如果你对偏函数理解不充分，可以看这篇的讨论
7. PEP 342 -- Coroutines via Enhanced Generators 协程和yield
8. PEP 380 -- Syntax for Delegating to a Subgenerator yield from语法
9. PEP 443 -- Single-dispatch generic functions Python 3的singledispatch装饰器
10. PEP 492 -- Coroutines with async and await syntax 协程与async/await语法
11. PEP 498 -- Literal String Interpolation Python 3.6新加的「格式化字符串字面量」，我看现在很多人都还不怎么用
12. PEP 525 -- Asynchronous Generators异步生成器
13. PEP 3101 -- Advanced String Formatting 字符串格式化
14. https://www.python.org/dev/peps/pep-3105/ 介绍为啥把print改成函数
15. PEP 3115 -- Metaclasses in Python 3000 Python3的元类
16. PEP 3119 -- Introducing Abstract Base Classes 抽象基类，不止一次看到有人用的abc模块都是错误的
17. PEP 3135 -- New Super Python 3中的super
18. PEP 3148 -- futures - execute computations asynchronously 我老提的concurrent.futures
19. PEP 3156 -- Asynchronous IO Support Rebooted: the asyncio Module 啥也不说了，asyncio模块