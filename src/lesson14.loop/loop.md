### Python3 循环语句
Python中的循环语句有 for 和 while。

Python循环语句的控制结构图如下所示：
![while_loop](/src/images/while_loop_1.png)
---
#### while 循环
Python中while语句的一般形式：
```
while 判断条件：
    语句
```
同样需要注意冒号和缩进。另外，在Python中没有do..while循环。

以下实例使用了 while 来计算 1 到 100 的总和：

##### 实例
```python
#!/usr/bin/env python3
 
n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))
```
执行结果如下：
```
1 到 100 之和为: 5050
```
#### 无限循环
我们可以通过设置条件表达式永远不为 false 来实现无限循环，实例如下：

##### 实例
```python
#!/usr/bin/python3
 
var = 1
while var == 1 :  # 表达式永远为 true
   num = int(input("输入一个数字  :"))
   print ("你输入的数字是: ", num)
 
print ("Good bye!")
```
输出结果如下：
```
输入一个数字  :5
你输入的数字是:  5
输入一个数字  :
```
你可以使用 **CTRL+C** 来退出当前的无限循环。

无限循环在服务器上客户端的实时请求非常有用。

#### while 循环使用 else 语句
在 while … else 在条件语句为 false 时执行 else 的语句块：

##### 实例
```python
#!/usr/bin/python3
 
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
```
输出结果如下：
```
0  小于 5
1  小于 5
2  小于 5
3  小于 5
4  小于 5
5  大于或等于 5
```
#### 简单语句组
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：

##### 实例
```python
#!/usr/bin/python
 
flag = 1
 
while (flag): print ('欢迎，欢迎!')
 
print ("Good bye!")
```
**注意**：以上的无限循环你可以使用 CTRL+C 来中断循环。

输出结果如下：
```
欢迎，欢迎!
欢迎，欢迎!
欢迎，欢迎!
欢迎，欢迎!
...
```
---
#### for 语句
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for循环的一般格式如下：
```
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```
Python loop循环实例：

##### 实例
```
>>>languages = ["C", "C++", "Perl", "Python"] 
>>> for x in languages:
...     print (x)
... 
C
C++
Perl
Python
>>>
```
以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：

##### 实例
```python
#!/usr/bin/python3
 
sites = ["Baidu", "Google","github","Taobao"]
for site in sites:
    if site == "github":
        print("sanm-zh!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
```
在循环到 "github"时会跳出循环体：
```
循环数据 Baidu
循环数据 Google
sanm-zh!
完成循环!
```

