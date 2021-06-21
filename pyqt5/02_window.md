

## 窗口类型

1. QMainWindow 主窗口
    + 菜单栏
    + 工具栏
    + 状态栏
    + 标题栏
2. QWidget
    + 是所有用户界面对象的基类，不确定是主窗口或对话框时可以使用。
    + 可以作为顶层窗口
    + 也可嵌入其他窗口
3. QDialog 
    + 对话框基类，执行短期任务
    + 可以是 模态 或 非模态
    + 无 菜单栏、工具栏、状态栏


>QMainWindow 不能设置布局(`setLayout()`)，因为有自己的布局。


## QLabel

继承关系

```
QObject ----+
            |
        QPaintDevice ----+
                         |
                         + ---- QFrame
                                   |
                                   +----- QLabel
```

## QDialog

子类有

+ QMessageBox
+ QFileDialog
+ QFontDialog
+ QInputDialog


