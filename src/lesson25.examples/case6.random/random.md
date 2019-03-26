[Python3 实例](/src/lesson25.examples/examples.md)
### Python 随机数生成

以下实例演示了如何生成一个随机数：

##### 实例
```python
# -*- coding: UTF-8 -*-
  
# 生成 0 ~ 9 之间的随机数
 
# 导入 random(随机数) 模块
import random
 
print(random.randint(0,9))
```
执行以上代码输出结果为：
```
4
```
以上实例我们使用了 random 模块的 randint() 函数来生成随机数，你每次执行后都返回不同的数字（0 到 9），该函数的语法为：
```
random.randint(a,b)
```
函数返回数字 N ，N 为 a 到 b 之间的数字（a <= N <= b），包含 a 和 b。

---
[Python3 实例](/src/lesson25.examples/examples.md)

---
#### 一个简单的随机数字小游戏
```python
#!/usr/bin/python
# -*- coding:utf-8 -*- 

#随机数字小游戏
import random
i = 1
a = random.randint(0,100)
b = int( input('请输入0-100中的一个数字\n然后查看是否与电脑一样：'))
while a != b:
    if a > b:
        print('你第%d输入的数字小于电脑随机数字'%i)
        b = int(input('请再次输入数字:'))
    else:
        print('你第%d输入的数字大于电脑随机数字'%i)
        b = int(input('请再次输入数字:'))
    i+=1
else:
    print('恭喜你，你第%d次输入的数字与电脑的随机数字%d一样'%(i,b))
```
