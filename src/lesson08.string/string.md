### Python3 字符串
字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。

创建字符串很简单，只要为变量分配一个值即可。例如：
```python
var1 = 'Hello World!'
var2 = "sanm-zh"
```
---
#### Python 访问字符串中的值
Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。

Python 访问子字符串，可以使用方括号来截取字符串，如下实例：

##### 实例(Python 3.0+)
```python
#!/usr/bin/python3
var1 = 'Hello World!'
var2 = "sanm-zh"
 
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
```
 
以上实例执行结果：
```
var1[0]:  H
var2[1:5]:  anm-
```
---
#### Python 字符串更新
你可以截取字符串的一部分并与其他字段拼接，如下实例：

##### 实例(Python 3.0+)
```python
#!/usr/bin/python3
 
var1 = 'Hello World!'
 
print ("已更新字符串 : ", var1[:6] + 'sanm-zh!')
```
以上实例执行结果
```
已更新字符串 :  Hello sanm-zh!
```
