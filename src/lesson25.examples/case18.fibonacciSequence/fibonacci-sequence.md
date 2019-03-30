[Python3 实例](/src/lesson25.examples/examples.md)
### Python 斐波那契数列

斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。

Python 实现斐波那契数列代码如下：

##### 实例
```python
# -*- coding: UTF-8 -*-
  
# Python 斐波那契数列实现
 
# 获取用户输入数据
nterms = int(input("你需要几项？"))
 
# 第一和第二项
n1 = 0
n2 = 1
count = 2
 
# 判断输入的值是否合法
if nterms <= 0:
   print("请输入一个正整数。")
elif nterms == 1:
   print("斐波那契数列：")
   print(n1)
else:
   print("斐波那契数列：")
   print(n1,",",n2,end=" , ")
   while count < nterms:
       nth = n1 + n2
       print(nth,end=" , ")
       # 更新值
       n1 = n2
       n2 = nth
       count += 1
```
执行以上代码输出结果为：
```
你需要几项？ 10
斐波那契数列：
0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 ,
```
---
[Python3 实例](/src/lesson25.examples/examples.md)