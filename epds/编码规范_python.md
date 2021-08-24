
## 行业要求

https://www.python.org/dev/peps/pep-0008/

## 缩进

仅使用空格，且为4个空格

## 行最大长度

行限制在最大 79 字符

折叠长行的首选方法是使用 Pyhon 支持的圆括号，方括号(brackets)和花括号(braces)内的行延续。如果需要，你可以在表达式周围增加一对额外的圆括号, 但是有时使用反斜杠看起来更好。确认恰当得缩进了延续的行。

## 空行

+ 用两行空行分割顶层函数和类的定义,类内方法的定义用单个空行分割。
+ 额外的空行可被用于(保守的(sparingly))分割一组相关函数(groups of related functions)。 在一组相关的单句中间可以省略空行。(例如.一组哑元(a set of dummy implementations))。
+ 当空行用于分割方法(method)的定义时，在`class`行和第一个方法定义之间也要有一个空行。
+ 在函数中使用空行时，请谨慎的用于表示一个逻辑段落(indicate logical sections)。 Python接受`contol-L`(即`^L`)换页符作为空格；Emacs(和一些打印工具) 视这个字符为页面分割符，因此在你的文件中，可以用他们来为相关片段(sections)分页。
 

## 命名规范

1. 包名、模块名、局部变量名、函数名
    + 全小写+下划线式驼峰 示例：`this_is_var`
2. 全局变量
    + 全大写+下划线式驼峰 示例：`GLOBAL_VAR`
3. 类名
    + 首字母大写式驼峰 示例：`ClassName()`
4. 变量名命名
    + 尽量体现变量的数据类型和具体意义
    >+ 变量名、类名取名必须有意义，严禁用单字母
    >+ 变量名不要用系统关键字，如 `dir` `type` `str` 等等
    >+ 建议：bool变量一般加上前缀 `is_` 如：`is_success`

## import 顺序

+ 1、标准库   2、第三方库  3、项目本身
+ 之间用空行分隔


__不建议__

```
import sys, os
```

__建议__

```
import sys
import os
from types import StringType, ListType
```



## models 内部定义顺序

+ `All database fields`
+ `Custom manager attributes`
+ `class Meta`
+ `def str()`
+ `def save()`
+ `def get_absolute_url()`
+ `Any custom methods`

## 异常捕获处理原则

尽量只包含容易出错的位置，不要把整个函数 try catch
对于不会出现问题的代码，就不要再用 try catch了
只捕获有意义，能显示处理的异常
能通过代码逻辑处理的部分，就不要用 try catch
异常忽略，一般情况下异常需要被捕获并处理，但有些情况下异常可被忽略，只需要用 log 记录即可，可参考一下代码：

```py
def ignored():
    try:
        yield
    except Exceptions as e:
        logger.warning(e)
        pass
```

## return early原则

提前判断并 return，减少代码层级，增强代码可读性(简单逻辑往前放)

```py
if not condition:
    return
# a lot if code
```

## Fat model， thin view

逻辑代码和业务代码解耦分离，功能性函数以及对数据库的操作定义写在 models 里面，业务逻辑写在 view里面。

## 权限校验装饰器异常抛出问题

建议权限不足时直接抛出异常，可以使用 django 自带的：

`from django.core.exceptions import PermissionDenied`

权限不足时抛出异常 PermissionDenied，之后应该返回什么样的页面由 handler 或者中间件去处理


## 分 method 获取 request 参数问题

一般可以分method 获取request参数，这样能够使代码更可读，且之后修改 method 时不必每个参数都修改

```py
args = request.GET if request.method == "GET" else request.POST
business_name = args.get('business_name', '')
template_name = args.get('template_name', '')
```

## 使用数字、常量表示状态

两种的话改为 `true/false`，多种改为 `enum` 可读性更好

```py
def enum(**enums):
    return type("Enum", (), enums)

StatusEnum = enum(
    SUCCESS=True,
    FAIL=False,
)
```

## Python 代码注释

方法必须使用标注注释，如果是公有方法或对外提供的 API 相关方法，则最好给出使用样例。如：

```py
def render_mako(template_name, dictionary={}, context_instance=None):
    """
    render the mako template and return the HttpResponse
    Args:
        template_name: 模板名字
        dictionary: context 字典
        context_instance: 初始化context ....
    Example:
        render_mako('mako_temp.html', {'form': form}, RequestContext(request))
    Returns:
        HttpResponse
    """

```

## Module注释：

在开头要加入对该模块的注释。如：

```py
"""
summary: 
usage:
```


## 其他注意问题

1. 【必须】去除代码中的 print，否则导致正式和测试环境 uwsgi 输出大量信息
2. 逻辑块空行分隔
3. 变量和其使用尽量放到一起
4. 【必须】 import过长，要放在多行的时候，使用 `from xxx import (a, b, c)`,不要用 `\` 换行
5. Django Model 定义的 choices 直接在定义在类里面




