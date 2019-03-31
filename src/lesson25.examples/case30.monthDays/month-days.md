[Python3 实例](/src/lesson25.examples/examples.md)
##### Python 计算每个月天数

以下代码通过导入 calendar 模块来计算每个月的天数：

##### 实例
```python
import calendar
monthRange = calendar.monthrange(2016,9)
print(monthRange)
```
执行以上代码输出结果为：
```
(3, 30)
```
输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数。以上实例输出的意思为 2016 年 9 月份的第一天是星期四，该月总共有 30 天。

---
[Python3 实例](/src/lesson25.examples/examples.md)

---
若只是想知道每个月的天数，可用：
```
>>> calendar.mdays
[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
```
##### 实例：
```python
import calendar
print(calendar.mdays[9])
```
