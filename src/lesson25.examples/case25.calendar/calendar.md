[Python3 实例](/src/lesson25.examples/examples.md)
### Python 生成日历

以下代码用于生成指定日期的日历：

##### 实例
```python
# 引入日历模块
import calendar
 
# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))
 
# 显示日历
print(calendar.month(yy,mm))
``` 
执行以上代码输出结果为：
```
输入年份: 2015
输入月份: 6
     June 2015
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
```
---
[Python3 实例](/src/lesson25.examples/examples.md)