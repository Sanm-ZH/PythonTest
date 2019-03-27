[Python3 实例](/src/lesson25.examples/examples.md)
### Python 判断闰年

以下实例用于判断用户输入的年份是否为闰年：

##### 实例
```python
# -*- coding: UTF-8 -*-
 
year = int(input("输入一个年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
       else:
           print("{0} 不是闰年".format(year))
   else:
       print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
else:
   print("{0} 不是闰年".format(year))
```
我们也可以使用内嵌 if 语句来实现：

执行以上代码输出结果为：
```
输入一个年份: 2000
2000 是闰年
输入一个年份: 2011
2011 不是闰年
```
---
[Python3 实例](/src/lesson25.examples/examples.md)

---
#### 参考方法：
```python
#!/usr/bin/python3

year = int(input("请输入一个年份："))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))
```

##### 但其实 Python 的 calendar 库中已经封装好了一个方法 isleap() 来实现这个判断是否为闰年：
```
>>> import calendar
>>> print(calendar.isleap(2000))
True
>>> print(calendar.isleap(1900))
False
```
根据用户输入判断：
```python
import calendar

year = int(input("请输入年份："))
check_year=calendar.isleap(year)
if check_year == True:
    print ("闰年")
else:
    print ("平年")
```
