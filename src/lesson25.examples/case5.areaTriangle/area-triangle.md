[Python3 实例](/src/lesson25.examples/examples.md)
### Python 计算三角形的面积

以下实例为通过用户输入三角形三边长度，并计算三角形的面积：

##### 实例
```python
# -*- coding: UTF-8 -*-
  
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))
 
# 计算半周长
s = (a + b + c) / 2
 
# 计算面积
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('三角形面积为 %0.2f' %area)
```
执行以上代码输出结果为：
```
$ python test.py 
输入三角形第一边长: 5
输入三角形第二边长: 6
输入三角形第三边长: 7
三角形面积为 14.70
```
---
[Python3 实例](/src/lesson25.examples/examples.md)