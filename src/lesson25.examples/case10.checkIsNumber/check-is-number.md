[Python3 实例](/src/lesson25.examples/examples.md)
### Python 判断字符串是否为数字

以下实例通过创建自定义函数 is_number() 方法来判断字符串是否为数字：

##### 实例
```python

# -*- coding: UTF-8 -*-
 
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
# 测试字符串和数字
print(is_number('foo'))   # False
print(is_number('1'))     # True
print(is_number('1.3'))   # True
print(is_number('-1.37')) # True
print(is_number('1e3'))   # True
 
# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # False
```
我们也可以使用内嵌 if 语句来实现：

执行以上代码输出结果为：
```
False
True
True
True
True
True
True
True
False
```
#### 更多方法
Python `isdigit()` 方法检测字符串是否只由数字组成。

Python `isnumeric()` 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。

---
[Python3 实例](/src/lesson25.examples/examples.md)